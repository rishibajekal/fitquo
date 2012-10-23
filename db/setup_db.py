# A script to clean and setup the tables in the database

from tornado.database import Connection
import sys

usage = """\

ERROR:
Please specify the stack in which you would like to run the database setup.

    "dev": to run locally
    "prod": to run on production
"""

dev_prompt = """\

The script will now try to connect to...
    database:   'fitquo'
    on host:    'localhost:3306'
    using user: 'root'

"""

prod_prompt = """\

The script will now try to connect to:
    database:   'fitquo'
    on host:    'FIXME'
    using user: 'fitquo'

"""

if len(sys.argv) != 2:
    print usage
    sys.exit(1)

stack = sys.argv[1]

if stack not in ('dev', 'prod'):
    print usage
    sys.exit(1)

if stack == "dev":
    print dev_prompt
    password = raw_input("Please type the password for this user: ")
    print password
    db = Connection(host="localhost:3306", database="fitquo", user="root", password="")
else:
    print prod_prompt
    password = raw_input("Please type the password for this user: ")
    db = Connection(host="FIXME", database="fitquo", user="fitquo", password=password)


# Drop existing tables
cmd = """\
DROP TABLE IF EXISTS `RelatesTo`;\
DROP TABLE IF EXISTS `SpecializesIn`;\
DROP TABLE IF EXISTS `Interests`;\
DROP TABLE IF EXISTS `FitnessTopics`;\
DROP TABLE IF EXISTS `Answer`;\
DROP TABLE IF EXISTS `Question`;\
DROP TABLE IF EXISTS `Trainer`;\
DROP TABLE IF EXISTS `User`;\
"""
db.execute(cmd)

# Create User table
cmd = """\
CREATE TABLE `User` (\
  `user_id` INT NOT NULL AUTO_INCREMENT,\
  `user_name` VARCHAR(100) NOT NULL DEFAULT 'NULL',\
  `fb_id` INT NOT NULL,\
  `user_email` VARCHAR(50) NULL DEFAULT NULL,\
  `age` INT NULL DEFAULT NULL,\
  `weight` INT NULL DEFAULT NULL,\
  `height` INT NULL DEFAULT NULL,\
  PRIMARY KEY (`user_id`),\
  UNIQUE (`fb_id`)\
);\
"""
db.execute(cmd)

# Create Trainer table
cmd = """\
CREATE TABLE `Trainer` (\
  `trainer_id` INT NOT NULL AUTO_INCREMENT,\
  `fb_id` INT NOT NULL,\
  `trainer_name` VARCHAR(50) NOT NULL DEFAULT 'NULL',\
  `trainer_email` VARCHAR(50) NOT NULL DEFAULT 'NULL',\
  `gym` VARCHAR(100) NULL DEFAULT NULL,\
  `certification` VARCHAR(150) NULL DEFAULT NULL,\
  PRIMARY KEY (`trainer_id`),\
  UNIQUE (`fb_id`)\
);\
"""
db.execute(cmd)

# Create Question table
cmd = """\
CREATE TABLE `Question` (\
  `question_id` INT NOT NULL AUTO_INCREMENT,\
  `user_ID` INT NOT NULL,\
  `posted_at` TIMESTAMP NOT NULL,\
  `content` VARCHAR(250) NOT NULL,\
  PRIMARY KEY (`question_id`),\
  FOREIGN KEY (user_ID) REFERENCES `User` (`user_id`)\
);\
"""
db.execute(cmd)

# Create Answer table
cmd = """\
CREATE TABLE `Answer` (\
  `answer_id` INT NOT NULL AUTO_INCREMENT,\
  `question_id` INT NOT NULL,\
  `trainer_id` INT NOT NULL,\
  `posted_at` TIMESTAMP NOT NULL,\
  `content` VARCHAR(250) NOT NULL,\
  `rating` INT NULL DEFAULT NULL,\
  PRIMARY KEY (`answer_id`),\
  FOREIGN KEY (question_id) REFERENCES `Question` (`question_id`),\
  FOREIGN KEY (trainer_id) REFERENCES `Trainer` (`trainer_id`)\
);\
"""
db.execute(cmd)

# Create FitnessTopics table
cmd = """\
CREATE TABLE `FitnessTopics` (\
  `topic_id` INT NOT NULL AUTO_INCREMENT,\
  `name` VARCHAR(50) NOT NULL,\
  PRIMARY KEY (`topic_id`)\
);\
"""
db.execute(cmd)

# Create Interests table
cmd = """\
CREATE TABLE `Interests` (\
  `interest_id` INT NOT NULL AUTO_INCREMENT,\
  `user_id` INT NOT NULL,\
  `topic_id` INT NOT NULL,\
  PRIMARY KEY (`interest_id`),\
  FOREIGN KEY (user_id) REFERENCES `User` (`user_id`),\
  FOREIGN KEY (topic_id) REFERENCES `FitnessTopics` (`topic_id`)\
);\
"""
db.execute(cmd)

# Create SpecializesIn table
cmd = """\
CREATE TABLE `SpecializesIn` (\
  `specin_id` INT NOT NULL AUTO_INCREMENT,\
  `trainer_id` INT NOT NULL,\
  `topic_id` INT NOT NULL,\
  PRIMARY KEY (`specin_id`),\
  FOREIGN KEY (trainer_id) REFERENCES `Trainer` (`trainer_id`),\
  FOREIGN KEY (topic_id) REFERENCES `FitnessTopics` (`topic_id`)\
);\
"""
db.execute(cmd)

# Create RelatesTo table
cmd = """\
CREATE TABLE `RelatesTo` (\
  `about_id` INT NOT NULL AUTO_INCREMENT,\
  `question_id` INT NOT NULL,\
  `topic_id` INT NOT NULL,\
  PRIMARY KEY (`about_id`),\
  FOREIGN KEY (question_id) REFERENCES `Question` (`question_id`),\
  FOREIGN KEY (topic_id) REFERENCES `FitnessTopics` (`topic_id`)\
);\
"""
db.execute(cmd)

db.close()

print "Database setup complete.\n"
