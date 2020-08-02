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

## Command Line/Unix Basics

Luckily, the basics of Unix is extremely easy to get comfortable with after some practice! There's very little to learn until you can start running some programs for your analysis.

First, we need to access a Bash Shell (Bash = Unix command language; Shell = command line interface). For mac and linux users, all you need to do is open the terminal application and you're good to go! Windows users need to download an application (many different versions exist) to access a Bash Shell.

What you'll first see when opening the command line is a prompt similar to `usr$` that usually corresponds to whatever your login username is on your computer. This prompt will change based on the directory you are in, which we will discuss in the next section!

### Directories and files 

The way your files are organized in the command line interface is exactly the same as they would be in 'Finder' or 'My Documents', just the way you access them is different. What you would normally experience in the GUI is a physical appearance of a folder, but for the command line, we call folders 'directories'. When we opened the command line, we started in our home directory. 

One of the most important concepts to understand is the *absolute file path* of a directory or file. It is as the name suggests - a path to get to your directory of interest. Use the `pwd` command (stands for 'print working directory') to see the absolute file path of the current directory.

```
username$ pwd
/Users/username
```

For many command line programs and R, you will need to specify the absolute file path for your files that you're interested in analyzing.

Now lets get comfortable with directories and filepaths by doing a small exercise. We will create a new directory with `mkdir` and then go into that directory and display the absolute file path. Note: 'spaces' in files and directories complicate things slightly, so it's best practice to just avoid them and use an underscore instead. 

```
username$ mkdir new_directory # creates a new directory called 'new_directory'
username$ cd new_directory # changes our current directory to 'new_directory'  
# It is important to mention that when we can only call 'new_directory' like this if it is located in our current directory, or else we'd have to specify the absolute file path of 'new_directory'
```

Now we'll explore our new directory. 

```
username$ ls # lists files in current directory

# it is blank which means there are no files in here, lets make one 
username$ nano
```

Welcome to nano, a basic text editor accessible in the command line. 

[image of nano]
(https://ben-cad.github.io/images/nano.png)


directories = folders
ls
ch
mkdir
head, tail, cat, nano
etc.

Unix command cheat sheet:




```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```


