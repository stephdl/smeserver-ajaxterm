#!/usr/bin/perl 

# mweinber Nov 2007

my $allowOnlyLocalhost = $0=~/login-localhost\.pl$/ ? 1 : 0;


my $host='localhost';
if( not $allowOnlyLocalhost )
	{
	print "Host [localhost]: ";
	$host=<STDIN>; chomp $host; $host = $host ? $host : 'localhost';
	}

my $local = ($host eq 'localhost') or ($host eq '127.0.0.1') ? 1 : 0;

my $port;
if( not $local )
	{
	print "SSH Port [22]: ";
	$port=<STDIN>; chomp $port; $port = $port ? $port : '22';
	}

print "Login [root]: ";
my $login=<STDIN>; chomp $login; $login = $login ? $login : 'root';

if( not $local )
	{
	system( "/usr/bin/ssh -p $port -o StrictHostKeyChecking=no $login\@$host" );
	}
else
	{
	system( "/bin/su - $login" );
	}

