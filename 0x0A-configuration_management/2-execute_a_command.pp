# pkill
exec { 'pkill':
path     => ['/usr/bin/', '/sbin/', '/bin/', '/usr/sbin/'],
provider => 'shell',
command  => 'pkill "killmenow"'
}
