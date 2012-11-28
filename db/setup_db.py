# A script to clean and setup the tables in the database

from tornado.database import Connection
import sys


def get_db_credentials():
    prompt = """\

Please enter the following information to connect to the database.

    """
    print prompt
    host = raw_input("'host': ")
    db = raw_input("'database name': ")
    user = raw_input("'username': ")
    password = raw_input("'password': ")
    return (host, db, user, password)


def print_connection_prompt(host, database, user):
    prompt = """\

The script will now try to connect to...
    database:   '%s'
    on host:    '%s'
    using user: '%s'

""" % (database, host, user)
    print prompt

host, db, user, password = get_db_credentials()
print_connection_prompt(db, host, user)
sure = raw_input('Are you sure? (yes/no) ')
if sure in ('yes', 'Yes', 'y', 'Y'):
    db = Connection(host=host, database=db, user=user, password=password)
else:
    print "Operation aborted."
    sys.exit(1)

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
  `user_email` VARCHAR(50) NULL DEFAULT NULL,\
  `age` INT NULL DEFAULT NULL,\
  `weight` INT NULL DEFAULT NULL,\
  `height` INT NULL DEFAULT NULL,\
  `address` VARCHAR(200) NOT NULL DEFAULT 'NULL',\
  `city` VARCHAR(150) NOT NULL DEFAULT 'NULL',\
  `state` VARCHAR(5) NOT NULL DEFAULT 'NULL',\
  PRIMARY KEY (`user_id`)
);\
"""
db.execute(cmd)

# Create Trainer table
cmd = """\
CREATE TABLE `Trainer` (\
  `trainer_id` INT NOT NULL AUTO_INCREMENT,\
  `trainer_name` VARCHAR(100) NOT NULL DEFAULT 'NULL',\
  `trainer_email` VARCHAR(50) NOT NULL DEFAULT 'NULL',\
  `gym` VARCHAR(100) NULL DEFAULT NULL,\
  `certification` VARCHAR(150) NULL DEFAULT NULL,\
  `address` VARCHAR(200) NOT NULL DEFAULT 'NULL',\
  `city` VARCHAR(150) NOT NULL DEFAULT 'NULL',\
  `state` VARCHAR(5) NOT NULL DEFAULT 'NULL',\
  PRIMARY KEY (`trainer_id`)
);\
"""
db.execute(cmd)

# Create Question table
cmd = """\
CREATE TABLE `Question` (\
  `question_id` INT NOT NULL AUTO_INCREMENT,\
  `user_id` INT NOT NULL,\
  `posted_at` VARCHAR(50) NOT NULL DEFAULT 'NULL',\
  `content` VARCHAR(250) NOT NULL,\
  PRIMARY KEY (`question_id`),\
  FOREIGN KEY (user_id) REFERENCES `User` (`user_id`)\
);\
"""
db.execute(cmd)

# Create Answer table
cmd = """\
CREATE TABLE `Answer` (\
  `answer_id` INT NOT NULL AUTO_INCREMENT,\
  `question_id` INT NOT NULL,\
  `trainer_id` INT NOT NULL,\
  `posted_at` VARCHAR(50) NOT NULL DEFAULT 'NULL',\
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
  `name` VARCHAR(100) NOT NULL,\
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

# Inserts topics into FitnessTopics
cmd = """\
INSERT INTO `FitnessTopics` (`name`)\
  VALUES\
  ("Aerobics"),\
  ("Bodybuilding"),\
  ("Cardio"),\
  ("Diet and Nutrition"),\
  ("Kickboxing"),\
  ("Plyometrics"),\
  ("Rehabilitation"),\
  ("Weight Loss"),\
  ("Yoga")\
;\
"""
db.execute(cmd)

db.close()

print "Database setup complete.\n"
