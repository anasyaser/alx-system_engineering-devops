<title>Project: 0x03. Shell, init files, variables and expansions | ALX Africa Intranet</title>

	<h2>Resources</h2>

	<p><strong>Read or watch</strong>:</p>

	<ul>
	<li><a href="https://intranet.alxswe.com/rltoken/oXnzBjLBA9t9dr7WuftdmQ" title="Expansions" target="_blank">Expansions</a> </li>
	<li><a href="https://intranet.alxswe.com/rltoken/PLSUQnBcKKU5eEgRfRDlug" title="Shell Arithmetic" target="_blank">Shell Arithmetic</a> </li>
	<li><a href="https://intranet.alxswe.com/rltoken/SvdGNZJjKsPghzZEhaWu4Q" title="Variables" target="_blank">Variables</a> </li>
	<li><a href="https://intranet.alxswe.com/rltoken/tqud57kjsSYgDfeZDlwl3g" title="Shell initialization files" target="_blank">Shell initialization files</a> </li>
	<li><a href="https://intranet.alxswe.com/rltoken/zCemKQ8f1CxmODIs9dmcWg" title="The alias Command" target="_blank">The alias Command</a> </li>
	<li><a href="https://intranet.alxswe.com/rltoken/wYrZr3t3DeAE8PpYHYWGiw" title="Technical Writing" target="_blank">Technical Writing</a></li>
	</ul>

	<p><strong>man or help</strong>:</p>

	<ul>
	<li><code>printenv</code></li>
	<li><code>set</code></li>
	<li><code>unset</code></li>
	<li><code>export</code></li>
	<li><code>alias</code></li>
	<li><code>unalias</code></li>
	<li><code>.</code></li>
	<li><code>source</code></li>
	<li><code>printf</code></li>
	</ul>

	<h2>Learning Objectives</h2>

	<p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/d8LWxAXk9_gsvpPw3ICdwQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

	<h3>General</h3>

	<ul>
	<li>What happens when you type <code>$ ls -l *.txt</code></li>
	</ul>

	<h3>Shell Initialization Files</h3>

	<ul>
	<li>What are the <code>/etc/profile</code> file and the <code>/etc/profile.d</code> directory</li>
	<li>What is the <code>~/.bashrc</code> file</li>
	</ul>

	<h3>Variables</h3>

	<ul>
	<li>What is the difference between a local and a global variable</li>
	<li>What is a reserved variable</li>
	<li>How to create, update and delete shell variables</li>
	<li>What are the roles of the following reserved variables: HOME, PATH, PS1</li>
	<li>What are special parameters</li>
	<li>What is the special parameter <code>$?</code>?</li>
	</ul>

	<h3>Expansions</h3>

	<ul>
	<li>What is expansion and how to use them</li>
	<li>What is the difference between single and double quotes and how to use them properly</li>
	<li>How to do command substitution with <code>$()</code> and backticks</li>
	</ul>

	<h3>Shell Arithmetic</h3>

	<ul>
	<li>How to perform arithmetic operations with the shell</li>
	</ul>

	<h3>The <code>alias</code> Command</h3>

	<ul>
	<li>How to create an alias</li>
	<li>How to list aliases</li>
	<li>How to temporarily disable an alias</li>
	</ul>

	<h3>Other <code>help</code> pages</h3>

	<ul>
	<li>How to execute commands from a file in the current shell</li>
	</ul>

	<h2>Requirements</h2>

	<h3>General</h3>

	<ul>
	<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
	<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
	<li>All your scripts should be exactly two lines long (<code>$ wc -l file</code> should print 2)</li>
	<li>All your files should end with a new line (<a href="http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789">why?</a>)</li>
	<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
	<li>A <code>README.md</code> file, at the root of the folder of the project, describing what each script is doing</li>
	<li>You are not allowed to use <code>&amp;&amp;</code>, <code>||</code> or <code>;</code></li>
	<li>You are not allowed to use <code>bc</code>, <code>sed</code> or <code>awk</code></li>
	<li>All your files must be executable</li>
	</ul>

	<h2>More Info</h2>

	<p>Read your <code>/etc/profile</code>, <code>/etc/inputrc</code> and <code>~/.bashrc</code> files.</p>

	<p>Look at some files in the <code>/etc/profile.d</code> directory.</p>

	<p>Note: You do not have to learn about <code>awk</code>, <code>tar</code>, <code>bzip2</code>, <code>date</code>, <code>scp</code>, <code>ulimit</code>, <code>umask</code>, or shell scripting, yet.</p>


	<h2 Tasks</h2>

    <h3 class="panel-title">
      0. &lt;o&gt;
    </h3>

    <p>Create a script that creates an alias.</p>

	<ul>
	<li>Name: <code>ls</code></li>
	<li>Value: <code>rm *</code></li>
	</ul>

	<pre><code>julien@ubuntu:/tmp/0x03$ ls
	0-alias  file1  file2
	julien@ubuntu:/tmp/0x03$ source ./0-alias 
	julien@ubuntu:/tmp/0x03$ ls
	julien@ubuntu:/tmp/0x03$ \ls
	julien@ubuntu:/tmp/0x03$ 
	</code></pre>

        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>0-alias </code></li>
        </ul>

    <h3 class="panel-title">
      1. Hello you
    </h3>


    <p>Create a script that prints <code>hello user</code>, where user is the current Linux user.</p>

	<pre><code>julien@ubuntu:/tmp/0x03$ id
	uid=1000(julien) gid=1000(julien) groups=1000(julien),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
	julien@ubuntu:/tmp/0x03$ ./1-hello_you 
	hello julien
	julien@ubuntu:/tmp/0x03$ 
	</code></pre>

        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>1-hello_you </code></li>
        </ul>

    <h3 class="panel-title">
      2. The path to success is to take massive, determined action
    </h3>


    <p>Add <code>/action</code> to the <code>PATH</code>.
	<code>/action</code> should be the last directory the shell looks into when looking for a program.</p>

	<pre><code>julien@ubuntu:/tmp/0x03$ echo $PATH
	/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
	julien@ubuntu:/tmp/0x03$ source ./2-path 
	julien@ubuntu:/tmp/0x03$ echo $PATH
	/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/action
	julien@ubuntu:/tmp/0x03$ 
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>2-path</code></li>
        </ul>

    <h3 class="panel-title">
      3. If the path be beautiful, let us not ask where it leads
    </h3>


    <p>Create a script that counts the number of directories in the <code>PATH</code>.</p>

	<pre><code>julien@ubuntu:/tmp/0x03$ echo $PATH
	/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
	julien@ubuntu:/tmp/0x03$ . ./3-paths 
	11
	julien@ubuntu:/tmp/0x03$ PATH=/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:::::/hello
	julien@ubuntu:/tmp/0x03$ . ./3-paths 
	12
	julien@ubuntu:/tmp/0x03$ 
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>3-paths</code></li>
        </ul>

    <h3 class="panel-title">
      4. Global variables
    </h3>


    <p>Create a script that lists environment variables.</p>

	<pre><code>julien@ubuntu:/tmp/0x03$ source ./4-global_variables
	CC=gcc
	CDPATH=.:~:/usr/local:/usr:/
	CFLAGS=-O2 -fomit-frame-pointer
	COLORTERM=gnome-terminal
	CXXFLAGS=-O2 -fomit-frame-pointer
	DISPLAY=:0
	DOMAIN=hq.garrels.be
	e=
	TOR=vi
	FCEDIT=vi
	FIGNORE=.o:~
	G_BROKEN_FILENAMES=1
	GDK_USE_XFT=1
	GDMSESSION=Default
	GNOME_DESKTOP_SESSION_ID=Default
	GTK_RC_FILES=/etc/gtk/gtkrc:/nethome/franky/.gtkrc-1.2-gnome2
	GWMCOLOR=darkgreen
	GWMTERM=xterm
	HISTFILESIZE=5000
	history_control=ignoredups
	HISTSIZE=2000
	HOME=/nethome/franky
	HOSTNAME=octarine.hq.garrels.be
	INPUTRC=/etc/inputrc
	IRCNAME=franky
	JAVA_HOME=/usr/java/j2sdk1.4.0
	LANG=en_US
	LDFLAGS=-s
	LD_LIBRARY_PATH=/usr/lib/mozilla:/usr/lib/mozilla/plugins
	LESSCHARSET=latin1
	LESS=-edfMQ
	LESSOPEN=|/usr/bin/lesspipe.sh %s
	LEX=flex
	LOCAL_MACHINE=octarine
	LOGNAME=franky
	[...]
	julien@ubuntu:/tmp/0x03$ 
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>4-global_variables</code></li>
        </ul>

    <h3 class="panel-title">
      5. Local variables
    </h3>


    <p>Create a script that lists all local variables and environment variables, and functions.</p>

	<pre><code>julien@ubuntu:/tmp/0x03$ . ./5-local_variables
	BASH=/bin/bash
	BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:histappend:interactive_comments:progcomp:promptvars:sourcepath
	BASH_ALIASES=()
	BASH_ARGC=()
	BASH_ARGV=()
	BASH_CMDS=()
	BASH_COMPLETION_COMPAT_DIR=/etc/bash_completion.d
	BASH_LINENO=()
	BASH_REMATCH=()
	BASH_SOURCE=()
	BASH_VERSINFO=([0]="4" [1]="3" [2]="46" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")
	BASH_VERSION='4.3.46(1)-release'
	CLUTTER_IM_MODULE=xim
	COLUMNS=133
	COMPIZ_CONFIG_PROFILE=ubuntu
	COMP_WORDBREAKS=$' \t\n"\'&gt;&lt;=;|&amp;(:'
	DBUS_SESSION_BUS_ADDRESS=unix:abstract=/tmp/dbus-Fg27Lr20bq
	DEFAULTS_PATH=/usr/share/gconf/ubuntu.default.path
	DESKTOP_SESSION=ubuntu
	[...]'
	julien@ubuntu:/tmp/0x03$ 
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>5-local_variables</code></li>
        </ul>

    <h3 class="panel-title">
      6. Local variable
    </h3>


    <p>Create a script that creates a new local variable.</p>

	<ul>
	<li>Name: <code>BEST</code></li>
	<li>Value: <code>School</code></li>
	</ul>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>6-create_local_variable</code></li>
        </ul>

    <h3 class="panel-title">
      7. Global variable
    </h3>


    <p>Create a script that creates a new global variable.</p>

	<ul>
	<li>Name: <code>BEST</code></li>
	<li>Value: <code>School</code></li>
	</ul>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>7-create_global_variable</code></li>
        </ul>

    <h3 class="panel-title">

    <p>Write a script that prints the result of the addition of 128 with the value stored in the environment variable <code>TRUEKNOWLEDGE</code>, followed by a new line.</p>

	<pre><code>julien@production-503e7013:~$ export TRUEKNOWLEDGE=1209
	julien@production-503e7013:~$ ./8-true_knowledge | cat -e
	1337$
	julien@production-503e7013:~$
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>8-true_knowledge</code></li>
        </ul>

    <h3 class="panel-title">

    <p>Write a script that prints the result of <code>POWER</code> divided by <code>DIVIDE</code>, followed by a new line.</p>

	<ul>
	<li><code>POWER</code> and <code>DIVIDE</code> are environment variables</li>
	</ul>

	<pre><code>julien@production-503e7013:~$ export POWER=42784
	julien@production-503e7013:~$ export DIVIDE=32
	julien@production-503e7013:~$ ./9-divide_and_rule | cat -e
	1337$
	julien@production-503e7013:~$
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>9-divide_and_rule</code></li>
        </ul>

    <h3 class="panel-title">
      10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath
    </h3>


    <p>Write a script that displays the result of <code>BREATH</code> to the power <code>LOVE</code></p>

	<ul>
	<li><code>BREATH</code> and <code>LOVE</code> are environment variables</li>
	<li>The script should display the result, followed by a new line</li>
	</ul>

	<pre><code>julien@production-503e7013:~/$ export BREATH=4
	julien@production-503e7013:~/$ export LOVE=3
	julien@production-503e7013:~/$ ./10-love_exponent_breath
	64
	julien@production-503e7013:~/$
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>10-love_exponent_breath</code></li>
        </ul>

    <h3 class="panel-title">
      11. There are 10 types of people in the world -- Those who understand binary, and those who do not
</h3>


    <p>Write a script that converts a number from base 2 to base 10.</p>

	<ul>
	<li>The number in base 2 is stored in the environment variable <code>BINARY</code></li>
	<li>The script should display the number in base 10, followed by a new line</li>
	</ul>

	<pre><code>julien@production-503e7013:~/$ export BINARY=10100111001
	julien@production-503e7013:~/$ ./11-binary_to_decimal
	1337
	julien@production-503e7013:~/$
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>11-binary_to_decimal</code></li>
        </ul>

    <h3 class="panel-title">
      12. Combination
    </h3>


    <p>Create a script that prints all possible combinations of two letters, except <code>oo</code>.</p>

	<ul>
	<li>Letters are lower cases, from <code>a</code> to <code>z</code></li>
	<li>One combination per line</li>
	<li>The output should be alpha ordered, starting with <code>aa</code></li>
	<li>Do not print <code>oo</code></li>
	<li>Your script file should contain maximum 64 characters</li>
	</ul>

	<pre><code>julien@ubuntu:/tmp/0x03$ echo $((26 ** 2 -1))
	675
	julien@ubuntu:/tmp/0x03$ ./12-combinations | wc -l
	675
	julien@ubuntu:/tmp/0x03$ 
	julien@ubuntu:/tmp/0x03$ ./12-combinations | tail -303 | head -10
	oi
	oj
	ok
	ol
	om
	on
	op
	oq
	or
	os
	julien@ubuntu:/tmp/0x03$ 
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>12-combinations</code></li>
        </ul>

    <h3 class="panel-title">
      13. Floats
    </h3>


    <p>Write a script that prints a number with two decimal places, followed by a new line.</p>

	<p>The number will be stored in the environment variable <code>NUM</code>.</p>

	<pre><code>ubuntu@ip-172-31-63-244:~/0x03$ export NUM=0
	ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
	0.00
	ubuntu@ip-172-31-63-244:~/0x03$ export NUM=98
	ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
	98.00
	ubuntu@ip-172-31-63-244:~/0x03$ export NUM=3.14159265359
	ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
	3.14
	ubuntu@ip-172-31-63-244:~/0x03$
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>13-print_float</code></li>
        </ul>

    <h3 class="panel-title">
      14. Decimal to Hexadecimal
    </h3>


    <p>Write a script that converts a number from base 10 to base 16.</p>

	<ul>
	<li>The number in base 10 is stored in the environment variable <code>DECIMAL</code></li>
	<li>The script should display the number in base 16, followed by a new line</li>
	</ul>

	<pre><code>julien@production-503e7013:~/$ export DECIMAL=16
	julien@production-503e7013:~/$ ./100-decimal_to_hexadecimal
	10
	julien@production-503e7013:~/$ export DECIMAL=1337
	julien@production-503e7013:~/$ ./100-decimal_to_hexadecimal | cat -e
	539$
	julien@production-503e7013:~/$ export DECIMAL=15
	julien@production-503e7013:~/$ ./100-decimal_to_hexadecimal | cat -e
	f$
	julien@production-503e7013:~/$
	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>100-decimal_to_hexadecimal</code></li>
        </ul>

    <h3 class="panel-title">
      15. Everyone is a proponent of strong encryption
    </h3>


    <p>Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.</p>

	<pre><code>julien@production-503e7013:~/shell/fun_with_the_shell$ cat quote
	"Everyone is a proponent of strong encryption."
	- Dorothy E. Denning
   julien@production-503e7013:~/shell/fun_with_the_shell$ ./101-rot13 &lt; quote
   "Rirelbar vf n cebcbarag bs fgebat rapelcgvba."
   - Qbebgul R. Qraavat
   julien@production-503e7013:~/shell/fun_with_the_shell$

	</code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>101-rot13</code></li>
        </ul>

    <h3 class="panel-title">
      16. The eggs of the brood need to be an odd number
    </h3>


    <p>Write a script that prints every other line from the input, starting with the first line.</p>

	<pre><code>ubuntu@ip-172-31-63-244:/$ \ls -1
   bin
   boot
   dev
   etc
   home
   initrd.img
   lib
   lib32
   lib64
   libx32
   lost+found
   media
   mnt
   opt
   proc
   root
   run
   sbin
   srv
   sys
   t
   #t#
   t~
   tmp
   usr
   var
   vmlinuz
   whoareyou
   ubuntu@ip-172-31-63-244:/$ \ls -1 | ./102-odd
   bin
   dev
   home
   lib
   lib64
   lost+found
   mnt
   proc
   run
   srv
   t
   t~
   usr
   vmlinuz
   ubuntu@ip-172-31-63-244:/$
   </code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>102-odd</code></li>
        </ul>

		<h3 class="panel-title">
17. I aem an instant star. Just add water and stir.
		</h3>


		<p>Write a shell script that adds the two numbers stored in the environment variables <code>WATER</code>  and <code>STIR</code>  and prints the result.</p>

	<ul>
   <li><code>WATER</code>  is in base <code>water</code></li>
   <li><code>STIR</code>  is in base <code>stir.</code></li>
   <li>The result should be in base <code>bestchol</code></li>
   </ul>

	<pre><code>julien@production-503e7013:~$ export WATER="ewwatratewa"
   julien@production-503e7013:~$ export STIR="ti.itirtrtr"
   julien@production-503e7013:~$ ./103-water_and_stir
   shtbeolhc
   julien@production-503e7013:~$
   </code></pre>


        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x03-shell_variables_expansions</code></li>
            <li>File: <code>103-water_and_stir</code></li>
        </ul>
