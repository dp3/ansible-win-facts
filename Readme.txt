Install Procedure
1. git clone ansible-win-facts
2. yum install redis 
3. systemctl enable redis
4. systemctl start redis
5. Generate a password hash for rediis `echo "redis-password-string" | sha256sum`
6. Add the hash on the 'requirepass' in the '/etc/redis.conf'
7.Add the line 'fact_caching_connection = <redis-ip>:6379:0:<redis-hash>' to the 'ansbile.cfg' 

Usage
To view the facts after running the role enter in the following in a terminal.
`ansible <HOST or GROUP>  -m debug -a "var=ansible_getFacts"`

To search for host for a signal program:
`ansible <HOST or GROUP> -m debug -a "var=hostvars[inventory_hostname]['ansible_getFacts']['<PROGRAM NAME>']"`

Use in an Ansible role 
1. To check if a program is installed and set the register variable
```
- name: get variables
  debug: var=hostvars[inventory_hostname]['ansible_getFacts']['<PROGRAM NAME>']
    register: <PROGRAM NAME>
```
2.  Next use the register with the ansible 'when' command. Below is an exaple that will run in cases of the program missing.
```
  when: hostvars[inventory_hostname]['ansible_getFacts']['<PROGRAM NAME>'] is undefined
```

Complete Example 
- name: get variables
  debug: var=hostvars[inventory_hostname]['ansible_getFacts']['Microsoft Office Professional Plus 2016']
  register: msoffice_check

- name: create  ms office dir
  win_file:
    path: C:\msoffice
    state: directory
  when: hostvars[inventory_hostname]['ansible_getFacts']['Microsoft Office Professional Plus 2016'] is undefined

- name: copy ms office dir to c drive
  win_copy:
    src:  /misc/software/msoffice2016/
    dest: C:\msoffice
  ignore_errors: yes
  when: hostvars[inventory_hostname]['ansible_getFacts']['Microsoft Office Professional Plus 2016'] is undefined

- name:  Install msoffice
  win_command: choco install msoffice.20.16.1.nupkg -y
  args:
    chdir: C:\msoffice
  ignore_errors: yes
  when: hostvars[inventory_hostname]['ansible_getFacts']['Microsoft Office Professional Plus 2016'] is undefined

- name: remove MS office dir
  win_file:
    path: C:\msoffice
    state: absent
  when: hostvars[inventory_hostname]['ansible_getFacts']['Microsoft Office Professional Plus 2016'] is defined
```
licensed under GPL  
