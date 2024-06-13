class nginx::configure {
  # Ensure Nginx package is installed
  package { 'nginx':
    ensure => installed,
  }

  # Manage Nginx service
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/nginx.conf'],
  }

  # Define Nginx configuration
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('nginx/nginx.conf.erb'),
    notify  => Service['nginx'],
  }

  # Set limits for open files
  file { '/etc/security/limits.conf':
    ensure  => file,
    content => @(END)
      * soft nofile 65536
      * hard nofile 65536
      END
  }

  # Update sysctl settings
  exec { 'sysctl-settings':
    command => 'sysctl -w net.core.somaxconn=65535',
    path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
    notify  => Service['nginx'],
  }

  exec { 'reload-sysctl':
    command     => 'sysctl -p',
    path        => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
    refreshonly => true,
  }
}

# Apply the configuration
include nginx::configure
