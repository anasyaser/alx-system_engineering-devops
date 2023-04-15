
# Table of Contents



<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="<https://intranet.alxswe.com/rltoken/aQmRB6ms-SDHUhqY0Rsa3g>" title="Permissions" target="<sub>blank</sub>">Permissions</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>chmod</code></li>
<li><code>sudo</code></li>
<li><code>su</code></li>
<li><code>chown</code></li>
<li><code>chgrp</code></li>
<li><code>id</code></li>
<li><code>groups</code></li>
<li><code>whoami</code></li>
<li><code>adduser</code></li>
<li><code>useradd</code></li>
<li><code>addgroup</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="<https://intranet.alxswe.com/rltoken/ku9cNLQc4XzHnVXH6YFE7A>" title="explain to anyone" target="<sub>blank</sub>">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>Permissions</h3>

<ul>
<li>What do the commands <code>chmod</code>, <code>sudo</code>, <code>su</code>, <code>chown</code>, <code>chgrp</code> do</li>
<li>Linux file permissions</li>
<li>How to represent each of the three sets of permissions (owner, group, and other) as a single digit</li>
<li>How to change permissions, owner and group of a file</li>
<li>Why can’t a normal user <code>chown</code> a file</li>
<li>How to run a command with root privileges</li>
<li>How to change user ID or become superuser<br></li>
</ul>

<h3>Other Man Pages</h3>

<ul>
<li>How to create a user</li>
<li>How to create a group</li>
<li>How to print real and effective user and group IDs</li>
<li>How to print the groups a user is in</li>
<li>How to print the effective userid</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>$ wc -l file</code> should print 2)</li>
<li>All your files should end with a new line (<a href="<http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789>">why?</a>)</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, describing what each script is doing</li>
<li>You are not allowed to use backticks, <code>&amp;&amp;</code>, <code>||</code> or <code>;</code></li>
<li>All your files must be executable</li>
</ul>

  </div>
</div>

<h2> Tasks</h2>

<h3>
0.  My name is Betty

</h3>


<p>Create a script that switches the current user to the user <code>betty</code>.</p>

<ul>
<li>You should use exactly 8 characters for your command (+1 character for the new line)</li>
<li>You can assume that the user <code>betty</code> will exist when we will run your script</li>
</ul>

<pre><code>julien@ubuntu:/tmp/h$ tail -1 0-iam<sub>betty</sub> | wc -c
9
julien@ubuntu:/tmp/h$
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>0-iam<sub>betty</sub></code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

1.  Who am I

</h3>

<p>Write a script that prints the effective username of the current user.</p>

<pre><code>julien@ubuntu:/tmp/h$ ./1-who<sub>am</sub><sub>i</sub>
julien
julien@ubuntu:/tmp/h$ 
</code></pre>
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
            <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
            <li>File: <code>1-who<sub>am</sub><sub>i</sub></code></li>
        </ul>

-------------------------------------------------------------------------------

<h3>

2.  Groups

</h3>
<p>Write a script that prints all the groups the current user is part of.</p>

<pre><code>julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$ 
</code></pre>

<p>Note: depending on the user, you will get a different output.</p>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>2-groups</code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

3.  New owner

</h3>

<p>Write a script that changes the owner of the file <code>hello</code> to the user <code>betty</code>.</p>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r&#x2013; 1 julien julien 30 Sep 20 14:23 3-new<sub>owner</sub>
-rw-rw-r&#x2013; 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$ sudo ./3-new<sub>owner</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r&#x2013; 1 julien julien 30 Sep 20 14:23 3-new<sub>owner</sub>
-rw-rw-r&#x2013; 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>3-new<sub>owner</sub> </code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

4.  Empty!

</h3>
<p>Write a script that creates an empty file called <code>hello</code>.</p>
    <p><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
	<li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
	<li>File: <code>4-empty</code></li>
    </ul>

<h3 class="panel-title">
<p>Write a script that adds execute permission to the owner of the file <code>hello</code>.</p>

<ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 28 Sep 20 14:26 5-execute
-rw-rw-r&#x2013; 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
julien@ubuntu:/tmp/h$ ./5-execute 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 28 Sep 20 14:26 5-execute
-rwxrw-r&#x2013; 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>5-execute</code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

5.  Multiple permissions

</h3>

<p>Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file <code>hello</code>.</p>

<ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 36 Sep 20 14:31 6-multiple<sub>permissions</sub>
-r&#x2013;r&#x2013;&#x2014; 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./6-multiple<sub>permissions</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 36 Sep 20 14:31 6-multiple<sub>permissions</sub>
-r-xr-xr&#x2013; 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>6-multiple<sub>permissions</sub></code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

6.  Everybody!

</h3>

<p>Write a script that adds execution permission to the owner, the group owner and the other users, to the file <code>hello</code></p>

<ul>
<li>The file <code>hello</code> will be in the working directory</li>
<li>You are not allowed to use commas for this script</li>
</ul>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 28 Sep 20 14:35 7-everybody
-rw-r&#x2013;&#x2014; 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./7-everybody 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 28 Sep 20 14:35 7-everybody
-rwxr-x&#x2013;x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>7-everybody</code></li>
</ul>

-------------------------------------------------------------------------------

<h3>


7.  James Bond

</h3>

<p>Write a script that sets the permission to the file <code>hello</code> as follows:</p>

<ul>
<li>Owner: no permission at all</li>
<li>Group: no permission at all</li>
<li>Other users: all the permissions</li>
</ul>

<p>The file <code>hello</code> will be in the working directory
You are not allowed to use commas for this script</p>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 28 Sep 20 14:40 8-James<sub>Bond</sub>
-rwxr-x&#x2013;x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./8-James<sub>Bond</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 28 Sep 20 14:40 8-James<sub>Bond</sub>
--&#x2013;&#x2014;rwx 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

  <p><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
      <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
      <li>File: <code>8-James<sub>Bond</sub></code></li>
  </ul>

-------------------------------------------------------------------------------

<h3>

8.  John Doe

</h3>

<p>Write a script that sets the mode of the file <code>hello</code> to this:</p>

<pre><code>-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
</code></pre>

<ul>
<li>The file <code>hello</code> will be in the working directory</li>
<li>You are not allowed to use commas for this script</li>
</ul>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>9-John<sub>Doe</sub></code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

9.  Look in the mirror

</h3>

<p>Write a script that sets the mode of the file <code>hello</code> the same as <code>olleh</code>’s mode.</p>

<ul>
<li>The file <code>hello</code> will be in the working directory</li>
<li>The file <code>olleh</code> will be in the working directory</li>
</ul>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 42 Sep 20 14:45 10-mirror<sub>permissions</sub>
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r&#x2013; 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ ./10-mirror<sub>permissions</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r&#x2013; 1 julien julien 42 Sep 20 14:45 10-mirror<sub>permissions</sub>
-rw-rw-r&#x2013; 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r&#x2013; 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ 
</code></pre>

<p>Note: the mode of <code>olleh</code> will not always be 664. Make sure your script works for any mode.</p>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>10-mirror<sub>permissions</sub></code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

10.  Directories

</h3>

<p>Create a script that adds execute permission to all subdirectories of the <strong>current directory</strong> for  the owner, the group owner and all other users.</p>

<p>Regular files should not be changed.</p>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories<sub>permissions</sub>
drwx-&#x2013;&#x2014; 2 julien julien 4096 Sep 20 14:49 dir0
drwx-&#x2013;&#x2014; 2 julien julien 4096 Sep 20 14:49 dir1
drwx-&#x2013;&#x2014; 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r&#x2013; 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./11-directories<sub>permissions</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories<sub>permissions</sub>
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir0
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir1
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r&#x2013; 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>11-directories<sub>permissions</sub></code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

11.  More directories

</h3>

<p>Create a script that creates a directory called <code>my<sub>dir</sub></code> with permissions 751 in the working directory.</p>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory<sub>permissions</sub>
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir0
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir1
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r&#x2013; 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./12-directory<sub>permission</sub> s
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory<sub>permissions</sub>
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir0
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir1
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x&#x2013;x 2 julien julien 4096 Sep 20 14:59 my<sub>dir</sub>
-rw-rw-r&#x2013; 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>12-directory<sub>permissions</sub></code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

12.  Change group

</h3>

<p>Write a script that changes the group owner to <code>school</code> for the file <code>hello</code></p>

<ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   34 Sep 20 15:03 13-change<sub>group</sub>
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir0
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir1
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x&#x2013;x 2 julien julien 4096 Sep 20 14:59 my<sub>dir</sub>
-rw-rw-r&#x2013; 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./13-change<sub>group</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      34 Sep 20 15:03 13-change<sub>group</sub>
drwx&#x2013;x&#x2013;x 2 julien julien    4096 Sep 20 14:49 dir0
drwx&#x2013;x&#x2013;x 2 julien julien    4096 Sep 20 14:49 dir1
drwx&#x2013;x&#x2013;x 2 julien julien    4096 Sep 20 14:49 dir2
drwxr-x&#x2013;x 2 julien julien    4096 Sep 20 14:59 my<sub>dir</sub>
-rw-rw-r&#x2013; 1 julien school   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>13-change<sub>group</sub></code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

13.  Owner and group

</h3>

<p>Write a script that changes the owner to <code>vincent</code> and the group owner to <code>staff</code> for all the files and directories in the working directory.</p>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   36 Sep 20 15:06 100-change<sub>owner</sub><sub>and</sub><sub>group</sub>
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir0
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir1
drwx&#x2013;x&#x2013;x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x&#x2013;x 2 julien julien 4096 Sep 20 14:59 my<sub>dir</sub>
-rw-rw-r&#x2013; 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./100-change<sub>owner</sub><sub>and</sub><sub>group</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 vincent staff   36 Sep 20 15:06 100-change<sub>owner</sub><sub>and</sub><sub>group</sub>
drwx&#x2013;x&#x2013;x 2 vincent staff 4096 Sep 20 14:49 dir0
drwx&#x2013;x&#x2013;x 2 vincent staff 4096 Sep 20 14:49 dir1
drwx&#x2013;x&#x2013;x 2 vincent staff 4096 Sep 20 14:49 dir2
drwxr-x&#x2013;x 2 vincent staff 4096 Sep 20 14:59 my<sub>dir</sub>
-rw-rw-r&#x2013; 1 vincent staff   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>100-change<sub>owner</sub><sub>and</sub><sub>group</sub></code></li>
</ul>

-------------------------------------------------------------------------------

<h3>

14.  Symbolic links

</h3>

<p>Write a script that changes the owner and the group owner of <code><sub>hello</sub></code> to <code>vincent</code> and <code>staff</code> respectively.</p>

<ul>
<li>The file <code><sub>hello</sub></code> is in the working directory</li>
<li>The file <code><sub>hello</sub></code> is a symbolic link</li>
</ul>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   44 Sep 20 15:12 101-symbolic<sub>link</sub><sub>permissions</sub>
-rw-rw-r&#x2013; 1 julien julien   23 Sep 20 14:25 hello
lrwxrwxrwx 1 julien julien    5 Sep 20 15:10 \_hello -&gt; hello
julien@ubuntu:/tmp/h$ sudo ./101-symbolic<sub>link</sub><sub>permissions</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      44 Sep 20 15:12 101-symbolic<sub>link</sub><sub>permissions</sub>
-rw-rw-r&#x2013; 1 julien julien      23 Sep 20 14:25 hello
lrwxrwxrwx 1 vincent  staff    5 Sep 20 15:10 \_hello -&gt; hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
      <ul>
	<li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
	  <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
	  <li>File: <code>101-symbolic<sub>link</sub><sub>permissions</sub></code></li>
      </ul>

-------------------------------------------------------------------------------

<h3>

15.  If only

</h3>

<p>Write a script that changes the owner of the file <code>hello</code> to <code>betty</code> only if it is owned by the user <code>guillaume</code>.</p>

<ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien    julien      47 Sep 20 15:18 102-if<sub>only</sub> 
-rw-rw-r&#x2013; 1 guillaume julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./102-if<sub>only</sub> 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      47 Sep 20 15:18 102-if<sub>only</sub> 
-rw-rw-r&#x2013; 1 betty  julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 
</code></pre>

<p><strong>Repo:</strong></p>
      <ul>
	<li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
	  <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
	  <li>File: <code>102-if<sub>only</sub> </code></li>
      </ul>

-------------------------------------------------------------------------------

<h3>

16.  Star Wars

</h3>

<p>Write a script that will play the StarWars IV episode in the terminal.</p>

<p><strong>Repo:</strong></p>
<ul>
  <li>GitHub repository: <code>alx-system<sub>engineering</sub>-devops</code></li>
    <li>Directory: <code>0x01-shell<sub>permissions</sub></code></li>
    <li>File: <code>103-Star<sub>Wars</sub></code></li>
</ul>
