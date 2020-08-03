## Welcome To My Tutorial!

When I started my graduate school journey, I had no previous experience coding with any programming language. In order to complete my microbiome-related thesis, I really needed to learn how all this crazy text works. After lots of effort, I was able to teach myself how to master the basics and allowed myself to use any bioinformatic software I thought useful. With this page, I will share some insights on how to use basic command line functions, particularly focusing on teaching skills that will assist in bioinformatic research. 

I will mostly cover Unix basics, R and R Studio, Python (in particular, BioPython), and some examples running some common bioinformatic software for each programming language. Hopefully I can share some useful tips and tricks that I wished I knew when started my bioinformatic journey! 

## Why Should You Learn This?

While it is true that there are plenty of graphical user interfaces (GUIs) and websites that can complete various bioinformatic tasks for you, learning how to use these programs on the command line can take your research to the next level. 

Using command line based programs instead of GUIs will:
- give you access to more software, providing you with significantly more options for data generation and analysis
- allow you to run analysis on a larger scale, in a more rapid, efficient, and reproducible fashion
- provide you with the option to run your analysis on high performance compute clusters, or cloud servers, to free up your computer's RAM for other tasks
- enlighten you with the satisfaction of troubleshooting coding errors  

## Quick Links

[Command Line/Unix Basics](## Command Line/Unix Basics)
 - [Exploring Directories and Files](### Exploring Directories and Files)
 - [Downloading and Using Command Line Bioinformatic Programs](### Downloading and Using Command Line Bioinformatic Programs)
 - [Unix-Based Executables](#### Unix-Based Executables)

## Command Line/Unix Basics

Luckily, the basics of Unix is extremely easy to get comfortable with after some practice! There's very little to learn until you can start running some programs for your analysis.

First, we need to access a Bash Shell (Bash = Unix command language; Shell = command line interface). For mac and linux users, all you need to do is open the terminal application and you're good to go! Windows users need to download an application (many different versions exist) to access a Bash Shell.

What you'll first see when opening the command line is a prompt similar to `usr$` that usually corresponds to whatever your login username is on your computer. This prompt will change based on the directory you are in, which we will discuss in the next section!

### Exploring Directories and Files 

The way your files are organized in the command line interface is exactly the same as they would be in 'Finder' or 'My Documents', just the way you access them is different. What you would normally experience in the GUI is a physical appearance of a folder, but for the command line, we call folders 'directories'. When we opened the command line, we started in our home directory. 

One of the most important concepts to understand is the *absolute file path* of a directory or file. It is as the name suggests - a path to get to your directory of interest. Use the `pwd` command (stands for 'print working directory') to see the absolute file path of the current directory.

```
username$ pwd
/Users/username
# username is our home directory, remember this!
```
*Note, whenever you put a # in code, everything after it on that line will be ignored!*
For many command line programs and R, you will need to specify the absolute file path for your files that you're interested in analyzing.

Now lets get comfortable with directories and filepaths by doing a small exercise. We will create a new directory with `mkdir` and then go into that directory and display the absolute file path. Note: 'spaces' in files and directories complicate things slightly, so it's best practice to just avoid them and use an underscore instead. 



```
username$ mkdir new_directory # creates a new directory called 'new_directory'
username$ cd new_directory # changes our current directory to 'new_directory'  
```

It is important to mention that we can only call 'new_directory' like this (with `cd`) if it is located in our current directory, or else we'd have to specify the absolute file path of 'new_directory'. When you aren't specifying the full absolute file path, it means we are using a relative file path that starts from our current directory.


Now we'll explore our new directory. 

```
username$ ls # lists files in current directory

# it is blank which means there are no files in here, lets make one 
username$ nano
```

Welcome to nano, a basic text editor accessible in the command line. 

![image of nano](images/nano.png)

This functions like any other basic text editor, except you can only use your keyboard, so no cursor to move your way around the document! 
Make a document similar the one shown in the picture and we'll go through a few commands to explore the text file we made. Hint: ^ = the control button on your keyboard and WriteOut is the save function.

There are a few functions to quickly visualize contents of a file. We'll run through a few of them below to see how they work.

```
username$ head doc.txt
a
b
c
d
e
f
g
h
i
j

username$ tail doc.txt
g
h
i
j
k
l
m
n
o
p

username$ cat doc.txt
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p

username$ grep "b" doc.txt
b
username$ grep -c "b" doc.txt # to count the number of lines instead of displaying the lines
1
```

These commands are simple, but are used so universely to explore files quickly. `head` prints the first ten lines, `tail` prints the last ten lines, while `cat` prints every line in a file. Rapid checks of output files from certain analyses are best done with `head` or `tail`. To search for patterns in your text file, `grep` is the go-to for Unix. It returns every line in your text file that matches the specified pattern. 

For every single command, e.g. `ls`, there will be additional arguments that you can specify, like I did with `grep -c`. These give additional functions and will be discussed later on in the tutorial for other commands. 

Tip: for those of you who are working with large files containing many sequences in FASTA format, you can use `grep -c ">" file_name` to count the number of sequences!

You can also use `nano file_name` to edit any text file that already exists. 

Now lets learn how to organize our files. We can rename and move files with `mv`, copy files with `cp`, and we'll eventually delete the file and directory.

```
# first we'll rename the file 
username$ mv doc.txt alphabet.txt
username$ ls # to see our renamed file
alphabet.txt
username$ cp alphabet.txt /Users/username # copying the file to our home directory
username$ rm alphabet.txt # to delete the file in our current directory
username$ ls # to see the file is removed

username$ cd ~ # change back into our home directory, ~ represents the home directory and is a great shortcut!
username$ rmdir new_directory # to remove a directory, it must be empty to do this however
```

Congratulations! These are the very basic commands of a Unix-based command line. The best advice I can give is to practice with these, and get comfortable with the organization and structure of the command line interface. I've found it easiest when starting out to think of directories as folders instead! Once you're confident with these easy functions, start exploring extra arguments for them like I showed with `grep` earlier if you're curious!

*Unix command cheat sheet:*

Command | Function
------- | -------
pwd | displays the current directory
mkdir | creates a new directory
cd | change directory ('~' represents home directory; '..' is the parent directory)
ls | lists all files in the directory
nano | opens up the nano text editor
head | displays the first ten lines of a file
tail | displays the last ten lines of a file
cat | displays all the text in a file
grep | searches for patterns in a file 
mv | can be used to move files to new directories and rename files
cp | copies files to a new directory
rm | deletes a file
rmdir | deletes an empty directory

### Downloading and Using Command Line Bioinformatic Programs

Most command line based softwares that you will use for biological analysis will be writted in either a Unix or a Python language. The python interpreter should be installed by default on your computer, but if you do find it missing or you're having issues, you can find the download [here](https://www.python.org/downloads/).

#### Unix-Based Executables

First we will go through installing and using Unix-based programs. Lets use MUSCLE alignment software as a teaching example; MUSCLE is an extremely popular multiple sequence alignment tool that is quick and easy to use. Download the appropriate version of MUSCLE [here](https://drive5.com/muscle/downloads.htm).

Now that you have downloaded the file, it is likely a compressed file as .tar or .tar.gz and we need to extract this file in order to use it. 

First, change into the directory where the MUSCLE download is and we will extract it.
```
# if the file is .tar
username$ tar -xf filename
# if the file is .tar.gz
username$ tar -zxf filename 
```

Technically, MUSCLE is now usable as an 'executable'! There should always be installation instructions for different programs on their respective download websites (some are simple like MUSCLE, and some take a little more work). There's a couple more things we should learn about how the command line works with executables. 

Remember how I mentioned earlier in the tutorial that we can only call for certain files or directories if it's somewhere contained in the current directory or we must specify the absolute file path right? The same applies to executables. We need to tell our computer where to find the executable before it can run it. Lets first change the name of our executable to make things easier and then try to run it.
```
username$ mv muscle_versionnumberx muscle # renaming complicated file name simply to muscle
username$ muscle
-bash: muscle: command not found
```

What? It didn't work, even though the file is in our current directory! *Usually, just by calling executables with no additional arguments, it opens the help output and is a great way to check if everything is installed properly.*
We have two options on how to run this file. Notice how we never had any executables show up in any of the directories we've explored previously for simple commands like `head` or `cd`? These commands are in fact executables, but they weren't located in our current working directories when we called for them. They worked because they were located in the `PATH` *environmental variable*. Try the code below to see what `PATH` is on your machine, and try to guess what this means!

```
username$ echo $PATH
```

The output of this code shows a list of absolute file paths that your computer searches for executables that you call. Cool right!? Now that we understand this, we have three options on how to run our MUSCLE executable:

1. We can use `mv` to move MUSCLE to a directory contained in `PATH`
2. We can change `PATH` by adding another directory to it
3. Use a different way to call MUSCLE 

You should have the tools to complete option #1 by using `mv`. Option #2 isn't the best choice most of the time, but can be useful later in your bioinformatic career when running very large scale analyses with multiple programs. See below on how to add absolute file paths on to `PATH`. *NOTE THIS IS TEMPORARY AND WILL BE RESET ONCE YOU CLOSE THE COMMAND LINE INTERFACE*
```
username$ export PATH=$PATH:/absolute/path/to/MUSCLE
username$ echo $PATH # to check if it worked
username$ muscle 
```
Calling MUSCLE here should give you the help output or basic usage guidelines, if not, your absolute path above was probably incorrect (try using pwd to ensure you had it right!)

Option #3 is the most simple, and is what I use most commonly for programs relying on a single executable file. All you have to do is change to the directory containing your executable file and type `./` before calling your executable. 
```
username$ cd directory/containing/muscle
username$ ./muscle
```

Remember `~` is home directory; `..` is one directory up (the parent directory), and now `.` is the current directory. So `./` basically means check for a file in the current directory (`.`), and ignore 'PATH' (`/`). 

Congratulations! With a little practice, you should be a master using Unix executables! This is half the battle though, since there are many great bioinformatic programs that are based on the Python language. 

#### Python Based Bioinformatic Programs


