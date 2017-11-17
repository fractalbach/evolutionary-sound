

Updating the Webpage
==========================================================================

Updating the webpage is built on a layer all of the functionality of the program.  If this javascript file were not included, you could theoretically use the entire program with the command line.  However, you must have the functionality in order to use this javascript.


Several Types of Events are handled in this file:

* Functions that can be used by buttons and other interactive things.
* changing actual HTML and Text on the webpage.
* changing attributes to various DOM elements.
* drawing onto a canvas.



Updating Interfaces
--------------------------------------------------------------------------

Currently, **updateInterface()** is the only function here.  This clumps together the various individual components that are usually updated together.  Button clicks will most probably call this function.

~~~ javascript 
var updateInterface = function () {
    changeSoundStatus(is_sound_on);
    changeTextWaveform(is_sound_on, osc.type);
    changeTextFrequency(is_sound_on, osc.frequency.value);
};
~~~

Changing Text
--------------------------------------------------------------------------


Here is where specific elements within the HTML document are targeted and changed.  The functions here are very dependent on the structure of the HTML and the unique IDs they have been given.


**changeSoundStatus(boolean)** tells you if the sound is ON or OFF.


~~~ javascript 
var changeSoundStatus = function (status) {
    var span = document.getElementById('sound_status');
    span.innerHTML = status.toString();
    span.className = status.toString();
};
~~~

**changeTextWaveform(boolean, string)** displays the type of waveform being used by given oscillator.  The string will most likely be derived from oscillator.type


~~~ javascript 
var changeTextWaveform = function (status, waveform) {
    document.getElementById('waveform_type').innerHTML = waveform;
    document.getElementById('waveform_type').className = boolHighL(status);
};
~~~

**changeTextFrequency(boolean, integer)** displays the oscillator's frequency.  However, this function would accept and display any integer given.


~~~ javascript 
var changeTextFrequency = function (status, frequency) {
    document.getElementById('span_frequency').innerHTML = frequency.toString();
    document.getElementById('span_frequency').className = boolHighL(status); 
};
~~~

Supporting Functions
--------------------------------------------------------------------------


Supporting Functions map values that are saved in objects, and converts them into a printable form (like a string).


For example, this function takes a boolean and converts it into "highlight" or "no highlight".  These are the names of classes in the CSS that style boxes different colors.


~~~ javascript 
var boolHighL = function (status) {
    if (status) {return 'Highlight';} 
    else        {return 'NoHighlight';}
};
~~~
