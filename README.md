# [Not Battleships](https://github.com/Fergus-Stonehouse/not_battleships
- Not Battleships is a basic game based on the Battelships board game

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

[Mockup Screenshots](#mockup-screenshots)

[UX](#ux)

- [Colour Scheme](#colour-scheme)

[User Stories](#user-stories)

- [New site Users](#new-site-users)
- [Returning Site Users](#returning-site-users)

[Features](#features)

- [Existing Features](#existing-features)
- [Future Features](#future-features)

[Testing](#testing)

[Deployment](#deployment)

- [Local vs Deployment](#local-vs-deployment)

[Credits](#credits)

- [Content and Code](#content-and-code)

- [Acknowledgments](#acknowledgements)

</details>

## Mockup Screenshots

Below are two mockup images of the Your Weather website created using the "Am I Responsive" website.

| Screenshot 1 | Screenshot 2 |
| :---: | :---: |
| ![screenshot](documentation/mockups/Am%20I%20Responsive1.png) | ![screenshot](documentation/mockups/Am%20I%20Responsive2.png) |

## UX

- The design for the game is limited to a basic white on black text based system, akin to a terminal output.

### Colour Scheme

- No specific color scheme was used as it appears entirely in a terminal environment: white text against a black background.

## User Stories

### New Site Users

- As a new site user, I would like to know what Not Battleships is.
- As a new site user, I would like to know how to play the game.
- As a new site user, I would like to keep the interface as simple as posssible.

### Returning Site Users

- As a returning site user, I would like to have a larger or smaller map.
- As a returning site user, I would like to have more or less ships.

## Features

### Existing Features

| Feature | Description | Screenshot |
| :---: | :---: | :---: |
| **Game Menu** | The Not Battleships comes with a basic introduction game menu | ![screenshot](documentation/features/) |
| **Game Instructions** | A quick summary of the game and how to play. | ![screenshot](documentation/features/modal.png) |
| **Dual Game Boards** | The game presents the player with two boards, one with their ships and where the computer has fired and the other to show where they haave fired and if it has resulted in a hit or a miss. | ![screenshot](documentation/features/input-box.png) |
| **Game Size** | The size of the game map can be changed upon starting a new game. | ![screenshot](documentation/features/modal.png) |
| **Numvber of Ships** | The number of ships for each side can be determined at the beginning of the game. | ![screenshot](documentation/features/input-box.png) |

### Future Features

- Traditional Ships
  - A feature that includes the classic Battleships boats
- Ship direction
  - A feature to display the ships in alternative directions - horizontal and vertical.

## Tools & Technologies Used

- [Python](https://www.python.org/) used for all coding for the program.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Heroku](https://heroku.com) used for hosting the deployed interactive element of the program.

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The site was deployed to GitHub Pages. The steps to deploy are as follows:

- In the [GitHub repository](https://github.com/boderg/your-weather), navigate to the Settings tab.
- From the source section drop-down menu, select the **Main** Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found [here](https://boderg.github.io/your-weather).

### Local vs Deployment

There are no notable differences between my local developed site and the Heroku deployed site.

## Credits

The following are credits to various people and technologies that have directly or otherwise assisted in the creation of the Your Weather site.

### Content and Code

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | Main page | interactive pop-up (modal) for the about section |
| [W3Schools](https://www.w3schools.com/howto/howto_css_switch.asp) | Main page | interactive toggle switch |
| [YouTube](https://www.youtube.com/watch?v=WZNG8UomjSI&t=1783s) | Main page | a source to get an idea of how to lay out the page |
| [Coding Nepal](https://www.codingnepalweb.com/weather-app-project-html-javascript/) | Main page | a source to get an idea for how to structure my javascript file |
| [Geeks for Geeks](https://www.geeksforgeeks.org/weather-app-using-vanilla-javascript/) | Main page | a source to get an idea for layout and structure my javascript file |
| [Toptal](https://www.toptal.com/software/definitive-guide-to-datetime-manipulation) | Javascript | conversion and parsing of unix time stamp |
| [Wikipedia](https://en.wikipedia.org/wiki/List_of_short_place_names) | Javascript | helped in determining whether name validation is needed or not |
| [Open Weather](https://openweathermap.org/) | API Data | api used to retrieve data for the site |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Chris Quinn](https://github.com/10xOXR) for their support throughout the development of this project.
- I would like to thank my previous Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their encouragement to continue my journey after my one project course had finished.
- I would like to thank [Code Institute](https://codeinstitute.net) for giving me the opportunity to complete the 4P course.
- I would like to thank the [Code Institute](https://codeinstitute.net) facilitator team [Iris Smok](https://github.com/Iris-Smok/Iris-Smok) and Irene Neville for their advice.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support and general information that helps with my studies.
- I would like to thank my family, for their support and understanding, for believing in me, and allowing me to make this transition into software development.