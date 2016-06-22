title: Ansible for DevOps
author:
  name: David Yim
  twitter: dyim42
  url: http://github.com/dyim42
output: presentation.html

--

# Ansible for DevOps #
## A gentle look into DevOps ##

--

### Who Am I ###
* Sr. Software Engineer, Deployment @ Pacific Biosciences
* Father to 2 beautiful kids
* Lover of open source technologies

--

### What is Ansible? ###
* Configuration Management Provisioning Tool that is built on python that uses
  SSH for all communications
* Similar to Chef, Puppet, and SaltStack

--

### What is DevOps? ###

* Automation and provisioning
* Deployment - tar, rsync, git, OS Packaging

--

### What is DevOps? ###

How about a story?

--

### What is DevOps? ###

You have John, the developer

<img src="http://i3.liverpoolecho.co.uk/incoming/article6706055.ece/ALTERNATES/s615b/2823543JPG.jpg" width="50%">

--

### What is DevOps? ###

You have Dan, the IT guy.

<img src="http://ecx.images-amazon.com/images/I/41hXIWXv0AL._AC_UL320_SR274,320_.jpg" width="50%">

--

### What is DevOps? ###

The Developer

John developed a really cool super duper web application that builds on
Boryana's web scraping app that scrapes web pages for power plans. 
<img src="http://www.clipartbest.com/cliparts/eiM/AA6/eiMAA6n9T.jpeg" width="50%">

--

### What is DevOps? ###


He gets commission for any plan sold through his website. He can see his millions
rolling in. 
<img src="http://image.shutterstock.com/z/stock-photo-dollars-pile-from-packs-of-money-d-134935061.jpg" width="80%">

--

### What is DevOps? ###

He completes version 1.0 and gives it to Dan, our IT guy to get
working on the production machines.
<img src="https://kimbeirneloans.files.wordpress.com/2015/06/giving.jpg" width="90%">

--

### What is DevOps? ###

The IT Guy

What the hell is the requirements? Documentation sucks, I guess I understand,
they want to be first to market. 
<img src="https://www.nila.org/wp-content/uploads/2015/06/Confusing.jpeg">

--

### What is DevOps? ###

Requirements? <br />
<img src="http://comps.canstockphoto.com/can-stock-photo_csp11709730.jpg" width="40%">

--

### What is DevOps? ###

And so we begin building the server up to serve up the application.<br />
<img src="http://images.all-free-download.com/images/graphiclarge/under_construction_clip_art_22790.jpg" width="40%">

--

### What is DevOps? ###

After a hours later, IT guy tries to start the application, doesn't work. Dan
goes to talk with John about what might be misconfigured. He gets a few pointers
and off Dan goes.

--

### What is DevOps? ###

After a week later...

--

### What is DevOps? ###

The application is all setup! Time to celebrate right? No. The customers have
complained about bugs and feature requests. John needs help so they hire his
friend Jim. 
* What about security?
* What about performance in scaling as the website gets more traffic?
* etc

--

### What is DevOps? ###


Jim spends some time trying to get his computer setup to run John's app. John
says
<br /><br />
<img src="http://skirblog.typepad.com/.a/6a00d8341cb55f53ef010536ace89f970b-800wi" width="5%">
It works on my computer". 
<img src="http://skirblog.typepad.com/.a/6a00d8341cb55f53ef0120a604af2c970c-800wi" width="5%">
<br /><br />
John spent about a week trying to get the development environment on Jim's computer working.

--

### What is DevOps? ###

* What problems do you see with this scenario?
* How many of you have experienced similar issues to this?

--

### What is configuration management?  ###

Consistently and automatically control your infrastructure at which you deploy
and scale your applications to meet the depends of your install base. Align
resources with specific policies and business goals. 

--

### Why do I need Configuration Management? ###
Do you...
* manually configure each machine by hand?
* manually deploy your code to a server?
* have a complicated software stack?
* have to spend hours (or days or even weeks) provisioning new servers?
* use shell scripts to configuration your machines?
* Check out this article: [Taste Test - Puppet, Chef, Saltstack, Ansible](https://valdhaus.co/books/taste-test-puppet-chef-salt-stack-ansible.html)

--

### Why use Ansible? ###
* It is pure written in our favorite language - It's Python!
* It is simple - Uses YAML
* Uses SSH exclusively
  * so no need to install a client
  * By default uses ssh and can switch to paramiko (python's ssh library) 
* works with Python >2.6 without anything else (Targets) (CentOS 6.0+ & Ubuntu 10.04+)

--

### Installing Ansible ###

Using your OS package manager
```shell
# ubuntu/debian
apt-get install ansible

# centos/rhel
# Install EPEL repo, then install
yum install ansible
```


Using Pip to install Ansible
```shell
pip install ansible
```
--

### Vagrant ###

Infrastructure as code. This gave us the ability to programmatically create
and control VMs. Now VMs are throw away system. Use for testing, development, or
simply try a software out without any commitments fast and secure. 

[Download Vagrant](http://www.vagrantup.com)

--

### Examples ###
Here are examples of what you can do
