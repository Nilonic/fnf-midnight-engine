# FNF midnight engine - Python-based FNF Engine

###### Disclaimer: this was written by ChatGPT, with some edits by me


##### [skip to install guide](https://github.com/spyspy69/fnf-midnight-engine#Installation-guide)

FNF midnight engine is a Python-based engine for creating mods for the game "Friday Night Funkin'". While it may not be the first or the last engine of its kind, our goal is to provide an accessible platform for developing mods with its simple-to-understand code. Please note that the engine is currently in heavy development and is subject to frequent changes. The appearance of the engine may not be optimal at the moment, but improvements are expected in the near future.

###### Sidenote: this is *not* a continuation of FNF+ OR a replacement for FNF+, it is simply a side project while i wait to get my PC repaired

## Features:

1. Easy modding: FNF midnight engine offers a straightforward approach to modding the game, allowing users to create and implement their own modifications easily.

2. Simple-to-understand code: The engine's codebase is designed to be easily comprehensible, making it accessible for developers of various skill levels to understand and modify the engine to suit their needs.

3. Ongoing development: The engine is actively being developed and improved, with the intention of enhancing its functionality and usability over time.

## Motivation:

The creation of FNF midnight engine stemmed from a personal challenge undertaken by me, the developer. While I am not going to explain why I did this, I embarked on this project with a sense of regret or difficulty. Despite this, I am committed to pushing forward and improving the engine.

## Credits:

This engine would not have been possible without the incredible work of the original developers of Friday Night Funkin'. Their dedication and creativity laid the foundation for the modding community to thrive. A special thanks to:

- [ninjamuffin99](https://twitter.com/ninja_muffin99): Original source code.
- [PhantomArcade3k](https://twitter.com/phantomarcade3k) and [Evilsk8r](https://twitter.com/evilsk8r): Art contributions.
- [Kawaisprite](https://twitter.com/kawaisprite): Music contributions.

We, at the midnight team, express our gratitude for their outstanding contributions.

Additionally, I would like to acknowledge the following individuals for their contributions to FNF midnight engine:

- Nilon (me!): Main developer and documenter of the FNF midnight engine project.

<!-- get your name here! just commit to the page-->

## How to Modify the Engine:

To modify the engine, follow these steps:

1. Ensure that Git is installed on your system.

2. Open the command prompt or terminal.

3. Run the following commands if you are using Windows:
```cmd
git clone https://github.com/spyspy69/fnf-midnight-engine
cd "fnf midnight engine"
```

4. Alternatively, if you are using Linux, execute these commands:
```sh
git clone https://github.com/spyspy69/fnf-midnight-engine
cd fnf\ midnight\ engine
```

5. After navigating to the engine's directory, open your preferred text editor to start modifying the code to suit your needs.

Feel free to explore the engine's codebase and make the necessary changes to customize the functionality as desired.

## The Roadmap

This roadmap outlines the planned development milestones for the FNF midnight engine project, providing an overview of the upcoming releases and their respective goals.

### Version 1.0.0 (Upcoming Release)

- Implement a basic mod loader: Introduce a modular system that allows users to easily load and install mods created with the engine. This functionality will enable players to customize various aspects of the game, such as characters, songs, charts, and even add new functionality.

- Improve and optimize code: Conduct a comprehensive code review and optimization process to enhance the engine's performance and efficiency. This will involve streamlining the codebase, eliminating unnecessary processes, and adopting best practices to ensure a smooth and responsive experience for mod creators and players.

- Provide in-depth details for mod making and installation: Create detailed documentation and tutorials that guide mod creators through the process of utilizing the engine effectively. These resources will cover topics such as creating custom charts, modifying visuals, and integrating new assets into the game. Additionally, clear instructions will be provided to facilitate the installation of mods for players.

### Version 1.1.0

- Bug fixes and glitch resolution: After the release of version 1.0.0, community feedback and bug reports will be collected and analyzed. This phase will focus on addressing any identified bugs, glitches, or technical issues to ensure a smoother and more enjoyable user experience. The development team will work diligently to fix reported problems and enhance the overall stability of the engine.

- Performance optimization: Building upon the feedback received from the community, efforts will be made to further optimize the engine's performance. This will involve identifying areas where improvements can be made, such as reducing loading times, enhancing frame rates, and minimizing memory usage. The goal is to create a highly optimized engine that provides a seamless and responsive modding experience.

As development progresses, additional features, improvements, and bug fixes will be incorporated based on user feedback and the evolving needs of the community. The roadmap will be continuously updated to reflect these changes, ensuring transparency and providing a clear direction for the future of FNF midnight engine.

## Contributions and Community Support

The FNF midnight engine project thrives on the contributions and support from the community. We appreciate and encourage individuals to actively participate in the development and improvement of the engine. There are several ways you can contribute:

### 1. Bug Reports and Issue Tracking

If you come across any bugs, glitches, or technical issues while using FNF midnight engine, we highly appreciate detailed bug reports. Please submit them through our issue tracking system on GitHub. Include relevant information such as steps to reproduce the issue, expected behavior, and any error messages encountered. Your reports will help us identify and address these issues promptly.

### 2. Feature Requests and Suggestions

We value your input and ideas for enhancing the functionality and user experience of FNF midnight engine. If you have a feature request or suggestion, please share it with us on our GitHub repository. Describe the feature or improvement you envision and provide any supporting details or examples. Your input will guide our development efforts and help shape the future direction of the engine.

### 3. Code Contributions

If you have coding skills and would like to contribute directly to the development of FNF midnight engine, you are welcome to submit pull requests on GitHub. Whether it's bug fixes, performance optimizations, or new features, your contributions are invaluable to the project. Please refer to our contribution guidelines in the repository for more information on how to get started.

### 4. Documentation and Tutorials

Clear and comprehensive documentation is essential for users to understand and utilize the capabilities of FNF midnight engine. If you have expertise in modding or specific aspects of the engine, you can contribute by improving our documentation or creating tutorials. This can include explaining modding concepts, providing code examples, or offering tips and tricks for creating mods. Submit your contributions through pull requests on our documentation repository.

### 5. Community Support

Engaging with the community and providing support to fellow users is highly appreciated. If you have experience with FNF midnight engine, consider joining our community forums, Discord server, or social media channels. Share your knowledge, help answer questions, and provide guidance to newcomers. By supporting each other, we can foster a vibrant and inclusive community around FNF midnight engine.

We are grateful for all contributions and community support. Together, we can make FNF midnight engine even better and empower modders to create amazing experiences within "Friday Night Funkin'".

## File Structure

The FNF Midnight Engine codebase follows a specific file structure to organize its components and assets. Here's an overview of the main directories and files:

- **Main Directory**: This directory contains the main executable file and any self-made libraries specific to the FNF Midnight Engine.

- **Assets Directory**: The assets directory houses various essential resources for the engine. It includes the following subdirectories and files:

  - **Backgrounds Directory**: This directory contains the backgrounds used in the main menu of the game within the FNF Midnight Engine. These backgrounds help create an immersive visual experience for players.

  - **Music Directory**: The music directory holds all the songs used in the game. Each song has its own folder, and within each folder, you can find relevant MP3 files for different instruments and vocal tracks. This structure allows for easy management and customization of the game's music within the FNF Midnight Engine.

  - **Charts Directory**: The charts directory stores all the charts for the songs in JSON format within the FNF Midnight Engine. Each song has its own folder, and within each folder, you can find the corresponding chart file. The chart files define the gameplay elements, such as the timing and sequence of notes, for each song within the FNF Midnight Engine.

  - **Stage Images Directory**: This directory contains the spritemaps for the stages used in the game within the FNF Midnight Engine. Each stage has its own folder, and within each folder, you can find both XML and PNG files representing the stage's visual elements. These files define the layout and appearance of the game's stages within the FNF Midnight Engine.

  - **Character Images Directory**: The character images directory stores the spritemaps for the characters in the game within the FNF Midnight Engine. Similar to the stage images directory, each character has its own folder, and within each folder, you can find both XML and PNG files representing the character's visual components. These files define the appearance and animations of the game's characters within the FNF Midnight Engine.

  - **Settings JSON File**: This file contains the game's settings in JSON format within the FNF Midnight Engine. It includes various configuration options and parameters that can be customized to modify the game's behavior within the FNF Midnight Engine.

The organized file structure of the FNF Midnight Engine helps streamline the development process and allows for easy management and customization of the game's assets and components within the FNF Midnight Engine.


## Installation Guide:

Follow these steps to install and set up the FNF Midnight Engine:

1. **Download the Engine:**
   - Option 1: Visit the [latest releases page](https://github.com/spyspy69/fnf-midnight-engine/releases/latest) on the FNF Midnight Engine GitHub repository. Download the latest release package that matches your operating system.
   - Option 2: Open a terminal or command prompt and execute the following command to clone the repository:
     ```
     git clone https://github.com/spyspy69/fnf-midnight-engine.git
     ```

2. **Install Python 3 or Greater:**
   - Ensure that you have Python 3 or a newer version installed on your system. If you don't have Python installed, you can download it from the official Python website: [python.org/downloads](https://www.python.org/downloads/).
   - Follow the installation instructions specific to your operating system to complete the Python installation process.

3. **Run the Engine:**
   - Open a terminal or command prompt and navigate to the directory where you downloaded or cloned the FNF Midnight Engine.
   - Execute the following command to run the engine:
     ```
     python main.py
     ```
   - The FNF Midnight Engine should launch and be ready for use.

4. **Enjoy Modding!**
   - With the FNF Midnight Engine successfully installed and running, you can now start creating and implementing your own mods for the game "Friday Night Funkin'". Use your preferred text editor to modify the code, assets, and configurations according to your modding requirements.

   - Refer to the provided documentation or community resources for more information on how to make the most of the FNF Midnight Engine and unleash your creativity.

Make sure to keep your FNF Midnight Engine installation up to date by regularly checking for new releases or pulling the latest changes from the official repository.