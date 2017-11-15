# Evolutionary Sound

*Evolutionary Sound* is an programming experiment that combines a genetic (or evolutionary) algorithm with the production of sound through human-computer interaction.  The program is written in Javascript, and the interface will be in HTML, so it will be usable by an updated web browser.  


You begin by selecting a generic synthesized tone, or uploading your own sound file.  This sound will be "the first generation".


The concept of DNA is represented by a list of pairs: function and value.  Each function applies an operation to the "first generation sound".  After all functions have been applied, the resulting sound is generated into a playable file that a human can listen to. 


With each "generation", the computer will randomly create a function or change an existing function.  This will change the "DNA" list.  After the DNA has been changed, the sound will play for the human.  The human selects "Yes, I like that", or "No! I don't like that".  This alludes to the process of "natural selection".


The process can be continued indefinitely until the human decides to save the sound or the DNA.  Since the DNA is a list of functions that are applied to the original sound, it can be used for the creation of other sounds as well!




Definition(s) of "Evolution" in the context of this project:

* one of a set of prescribed movements
* :descent with modification from preexisting species 
* :cumulative inherited change in a population of organisms through time leading to the appearance of new forms 
* :the process by which new species or populations of living things develop from preexisting forms through successive generations

"Evolution." Merriam-Webster.com. Accessed November 14, 2017. https://www.merriam-webster.com/dictionary/evolution.








## Overview of Parts (Outline):

* Constants: 
    - default effects and functions that can change sound. 
    - Each function/effect should have a 'reccomended' value range, so that the random value doesn't ruin the sound.
    - range of human hearing (20 hz - 2000 hz) ? TODO: CONFIRM.
* Initial Sound:
    - option to import a sound from file - allow different filetypes
    - option to start with a generic tone.
    - maybe add a few instruments like piano with different notes.
* Constructing and Deconstructing Sound file
    - byte stream is easier for the genetic algorithm and functions.
    - sound file is easier for the computer to play the sound.
    - Function: Sound File  ->  ByteStream
    - Function: ByteStream  ->  Sound File 
* Genetic Algorithm:
    - glorifed random number generator.
    - Randomly selects a function
    - Randomly assigns a value to go with that function. 
    - Use the 'reccomended' value range from the constants, so that each generation is a reasonably subtle change, and doesn't result in useless sound.
* Memory
    - DNA in memory with each generation.
    - Original sound in memory.
    - Sound from last generation (to quickly generate the new sound).
    - Sound from current generation (so that you can play it).
* Data Storage
    - Save the DNA file with functions, and the original sound.
    - Save to CACHE, and/or download a JSON file.
    - Send Usage Data to somewhere for research purposes (Collect absolutely NO personal data. Only collect information about the randomly generated functions themselves.)
    - export the most recently created sound
* Interface (Webpage)
    - Startup page includes details about project and way to select sound
    - Button(s) for selecting if you like the sound or not.
    - Button to Play or Replay the most recent sound (or the original sound).





## Some Random Code:

~~~ javascript

const effectsList = {};
const functionsList = {(func1, range1) };

var sound = function (fileInput) {
    if (fileInput !== null) {
        this.file = fileInput;
        this.data = getDataFromFile(fileInput);
    }
};

var DNA = function (soundIn, blockIn) {
    this.sound = soundIn;
    this.block = blockIn;

};

var block = function () {

};

var getDataFromFile = function (fileInput) {
    pass
};
~~~