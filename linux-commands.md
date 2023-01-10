## Linux Directory Commands
### 1. pwd Command
The pwd command is used to display the location of the current working directory.
Syntax:
Pwd

### 2. mkdir Command

The mkdir command is used to create a new directory under any directory.
Syntax:
1. mkdir &lt;directory name&gt;  

### 3. rmdir Command
The rmdir command is used to delete a directory.
Syntax:
1. rmdir &lt;directory name&gt;  

### 4. ls Command
The ls command is used to display a list of content of a directory.
Syntax:
ls
### 5. cd Command
The cd command is used to change the current directory.
Syntax:
1. cd &lt;directory name&gt;  
## Linux File commands
### 6. touch Command
The touch command is used to create empty files. We can create multiple empty files by
executing it once.
Syntax:
1. touch &lt;file name&gt;  
### 7. cat Command
The cat command is a multi-purpose utility in the Linux system. It can be used to create a
file, display content of the file, copy the content of one file to another file, and more.
Syntax:

1. cat [OPTION]... [FILE]..  
To create a file, execute it as follows:
1. cat &gt; &lt;file name&gt;  
// Enter file content  
Press &quot;CTRL+ D&quot; keys to save the file. To display the content of the file, execute it as
follows:
cat &lt;file name&gt;  
### 8. rm Command
The rm command is used to remove a file.
Syntax:
rm &lt;file name&gt;
### 9. cp Command
The cp command is used to copy a file or directory.
Syntax:
To copy in the same directory:
cp &lt;existing file name&gt; &lt;new file name&gt;  
### 10. mv Command
The mv command is used to move a file or a directory form one location to another location.
Syntax:
1. mv &lt;file name&gt; &lt;directory path&gt;  

## Linux File Content Commands
### 11. head Command
The head command is used to display the content of a file. It displays the first 10 lines of a
file.
Syntax:
1. head &lt;file name&gt;  
### 12. tail Command
The tail command is similar to the head command. The difference between both commands is
that it displays the last ten lines of the file content. It is useful for reading the error message.

Syntax:
1. tail &lt;file name&gt;  
### 13. tac Command
The tac command is the reverse of cat command, as its name specified. It displays the file
content in reverse order (from the last line).
Syntax:
1. tac &lt;file name&gt;  
### 14. more command
The more command is quite similar to the cat command, as it is used to display the file
content in the same way that the cat command does. The only difference between both
commands is that, in case of larger files, the more command displays screenful output at a
time.
In more command, the following keys are used to scroll the page:
ENTER key: To scroll down page by line.
Space bar: To move to the next page.
b key: To move to the previous page.
/ key: To search the string.
Syntax:
1. more &lt;file name&gt;  
### 15. less Command
The less command is similar to the more command. It also includes some extra features such
as &#39;adjustment in width and height of the terminal.&#39; Comparatively, the more command cuts
the output in the width of the terminal.
Syntax:
1. less &lt;file name&gt;  

## Linux User Commands
### 16. The su command provides administrative access to another user. In other words, it allows
access of the Linux shell to another user.
Syntax:
1. su &lt;user name&gt;  
### 17. id Command
The id command is used to display the user ID (UID) and group ID (GID).
Syntax:

1. id  
### 18. useradd Command
The useradd command is used to add or remove a user on a Linux server.
Syntax:
1. useradd  username  
### 19. passwd Command
The passwd command is used to create and change the password for a user.
Syntax:
1. passwd &lt;username&gt; 
### 20. groupadd Command
The groupadd command is used to create a user group.
Syntax:
1. groupadd &lt;group name&gt;  
## Linux Filter Commands

### 22. cut Command
The cut command is used to select a specific column of a file. The &#39;-d&#39; option is used as a
delimiter, and it can be a space (&#39; &#39;), a slash (/), a hyphen (-), or anything else. And, the &#39;-f&#39;
option is used to specify a column number.
Syntax:
1. cut -d(delimiter) -f(columnNumber) &lt;fileName&gt;  

### 23. comm Command
The &#39;comm&#39; command is used to compare two files or streams. By default, it displays three
columns, first displays non-matching items of the first file, second indicates the non-matching
item of the second file, and the third column displays the matching items of both files.
Syntax:
1. comm &lt;file1&gt; &lt;file2&gt;  
### 24. tee command
The tee command is quite similar to the cat command. The only difference between both
filters is that it puts standard input on standard output and also write them into a file.
Syntax:
1. cat &lt;fileName&gt; | tee &lt;newFile&gt; |  cat or tac |.....  
### 25. tr Command
The tr command is used to translate the file content like from lower case to upper case.

Syntax:
1. command | tr &lt;&#39;old&#39;&gt; &lt;&#39;new&#39;&gt;  
### 26. uniq Command
The uniq command is used to form a sorted list in which every word will occur only once.
Syntax:
1. command &lt;fileName&gt; | uniq  
### 27. wc Command
The wc command is used to count the lines, words, and characters in a file.
Syntax:
1. wc &lt;file name&gt;  
### 28. od Command
The od command is used to display the content of a file in different s, such as hexadecimal,
octal, and ASCII characters.
Syntax:
1. od -b &lt;fileName&gt;      // Octal format  
2. od -t x1 &lt;fileName&gt;   // Hexa decimal format  
3. od -c &lt;fileName&gt;     // ASCII character format
### 29. sort Command
The sort command is used to sort files in alphabetical order.
Syntax:
1. sort &lt;file name&gt;  
### 30. gzip Command
The gzip command is used to truncate the file size. It is a compressing tool. It replaces the
original file by the compressed file having &#39;.gz&#39; extension.
Syntax:
1. gzip &lt;file1&gt; &lt;file2&gt; &lt;file3&gt;...  
## Linux Utility Commands
### 31. find Command
The find command is used to find a particular file within a directory. It also supports various
options to find a file such as byname, by type, by date, and more.
The following symbols are used after the find command:
(.) : For current directory name
(/) : For root

Syntax:
1. find . -name &quot;*.pdf&quot;  
### 32. locate Command
The locate command is used to search a file by file name. It is quite similar to find command;
the difference is that it is a background process. It searches the file in the database, whereas
the find command searches in the file system. It is faster than the find command. To find the
file with the locates command, keep your database updated.
Syntax:
1. locate &lt;file name&gt;  
### 33. date Command
The date command is used to display date, time, time zone, and more.
Syntax:
1. date  
### 34. cal Command
The cal command is used to display the current month&#39;s calendar with the current date
highlighted.
Syntax:
1. cal&lt;  
### 35. sleep Command
The sleep command is used to hold the terminal by the specified amount of time. By default,
it takes time in seconds.
Syntax:
sleep &lt;time&gt; 
### 36. time Command
The time command is used to display the time to execute a command.
Syntax:
time  
### 37. zcat Command
The zcat command is used to display the compressed files.
Syntax:
zcat &lt;file name&gt;  
### 38. df Command
The df command is used to display the disk space used in the file system. It displays the
output as in the number of used blocks, available blocks, and the mounted directory.
Syntax:

df  
### 39. mount Command
The mount command is used to connect an external device file system to the system&#39;s file
system.
Syntax:
mount -t type &lt;device&gt; &lt;directory&gt;  
### 40. exit Command
Linux exit command is used to exit from the current shell. It takes a parameter as a number
and exits the shell with a return of status number.
Syntax:
exit  
### 41. clear Command
Linux clear command is used to clear the terminal screen.
Syntax:
clear  
After pressing the ENTER key, it will clear the terminal screen.

## Linux Networking Commands
### 42.ip Command
Linux ip command is an updated version of the ipconfig command. It is used to assign an IP
address, initialize an interface, disable an interface.
Syntax:
ip a or ip addr  
### 43. ssh Command
Linux ssh command is used to create a remote connection through the ssh protocol.
Syntax:
ssh user_name@host(IP/Domain_name)&lt;/p&gt;  
### 44. mail Command
The mail command is used to send emails from the command line.
Syntax:
mail -s &quot;Subject&quot; &lt;recipient address&gt;  
### 45. ping Command

The ping command is used to check the connectivity between two nodes, that is whether the
server is connected. It is a short form of &quot;Packet Internet Groper.&quot;
Syntax:
ping &lt;destination&gt; 
### 46. host Command
The host command is used to display the IP address for a given domain name and vice versa.
It performs the DNS lookups for the DNS Query.
Syntax:
host &lt;domain name&gt; or &lt;ip address&gt;
