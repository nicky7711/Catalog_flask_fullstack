# Catalog
## About
Catalog is an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.
## How to run
1. Install Vagrant and VirtualBox
2. Download my files
3. Launch the Vagrant VM (Vagrant up)
4. Connect to the VM (Vagrant ssh)
5. Run cd /vagrant first, then navigate to the Catalog project path
6. Start the server (Python project.py)
7. Go to http://localhost:5000/
8. Have fun!

## Remark
* It is completely optional to put your own Google OAuth API key to run the application.
* In case database is not properly setup, you can delete and rerun *database_setup.py* first.
* In case you want to populate some dummy data, you can run *lotsofmenus.py*
