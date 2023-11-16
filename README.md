!

# PORTFOLIO 3 - "Travel Survey"

This is a travel survey designed for a company who wants to gain insights into how their employees travel to work each day, to help them decide if they should encourage more employees to work from home. The data collected informs them the average distance emplyees travel and the different modes of transport they use.

The deployed app can be found [here](https://travel-survey-d72fc1637c7d.herokuapp.com/)

---

## CONTENTS

- [PORTFOLIO 3 - "Travel Survey"](#portfolio-3---travel survey)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
      - [First Time Visitor Goals](#first-time-visitor-goals)
  - [Features](#features)
    - [Future Implementations](#future-implementations)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Testing](#testing)
  - [Credits](#credits)
    - [Code Used](#code-used)
    - [Content](#content)
    - [ Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### User Stories

#### First Time Visitor Goals

- To be able to quickly fill in the survey without error
- For the employers to easily be able to gain insights from the survey results

## Features

The program is connected to a Google Sheets document featuring 4 pages. 
The app intially asks a question about the distance travelled to work each day. This information is sent to the distances worksheet, the app then runs a function to create a tally of the distances travelled and the number of employees that travel each distance, these will then be plotted on a graph in Google Sheets. This allows the employers to visually see the distribution of the distance each employee travels.
The app then asks a series of questions about the mode of transport of the employees, asking how many times a week they walk/cycle/train/bus/drive/car pool. These results are sent to the transport worksheet, the sum of these results is sent to the transport_results worksheet where it is plotted on a pie chart in google sheets, allowing the employer to easily see which modes of transport are used most.

## Future Implementations

In future I would like to add a feedback option, where users can provide their thoughts on working from home and how they think it would effect their productivity and enjoyment of work.

### Accessibility

We have actively tried to ensure the app is accessible friendly as possible, we achieved this by:
- Messages are sent to the user while data is being collected and processed so that it is clear the app is working
- Error messages are sent with a clear explaination of the type of error the user has made
- Clear instructions are given before each user input to help ensure no errors are made

## Technologies Used

### Languages Used

Python

### Frameworks, Libraries & Programs Used

Git - for version control
Github - to save and store files
Heroku - for deployment 

## Deployment & Local Development

### Deployment

The site is deployed using Heroku and GitHub. Visit the deployed site [here](https://travel-survey-d72fc1637c7d.herokuapp.com/). To deploy using Heroku pages:

Login or Sign Up to Heruku.
Click "Create New app" button, and choose a unique name for the application.
Click on "Settings" on the navigation bar.
Add config vars for the creds.json file that won't be found on GitHub, to do this click "add congig vars" enter the key as "CREDS" and copy and paste the creds,json file into value and click add.
Add an additional config var with the key "PORT" and value "8000".
Now add relevent build packs, these are python and node.js. Ensure phython is listed first after they have been added.
Now click on the deployment tab, and select deploy from GitHub.
Login to GitHub and search for the repository name "travel_survey". The repository can also be found [here](https://github.com/sacarr98/travel_survey)
Then scroll down and click deploy and wait for the app to be deployed!

### Local Development

#### How to Fork

To fork the repository:
- Log in to Github
- Go to the repository for this project 
- Click the Fork button in the top right corner

#### How to Clone

To clone the repository:
- Log in to GitHub
- Go to the repository for this project
- Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

Testing documentation can be found [here](TESTING.md)

## Credits

### Code Used

The code was written by myself with some parts being taken from the Love Sandwiches project - for example the testing of inputs.

### Content

The content for the site was created by myself.

###  Acknowledgments

Thanks to the tutors at Code Institute for always being on hand when I needed some help with my code, and to my mentor for their guidence and advice.