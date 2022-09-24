# Songbook user manual

## Adding songs

The idea is that the songs can be easily moved around in the main .tex file. That's why songs should be defined in the ```songlist.sty``` file as commands that can be added to ```main.tex```. An example of a "song command":
```
\NewDocumentCommand{\jarjestoasiantuntija}{m}{
\begin{song}{#1}{Järjestöasiantuntijan runtulaulu}[\textit{Sävel:} Песенка крокодила Гены]

\begin{songverse}
Fuksit oksentaa rappuun,

kaljatölkkejä tippuu

parvekkeelta alas asfalttiin.

Sitten järjestysmieskin 

tappelee uuden eessä.

Kertoo vartijaraporttini niin.
\end{songverse}

\begin{songchorus}

Minä annan käyttökiellon,

järjestöt on kauhuissaan.

\begin{repeatable}
Voisin viettää runtupäivää

jälleen huomenna
\end{repeatable}

\end{songchorus}

\end{song}
}
```

Here we define a new document command ```jarjestoasiantuntija``` with one mandatory parameter. Inside the third pair of curly brackets we define the song.
The whole song should be inside the ```song``` environment for which we give the one mandatory argument. The ```song``` environment also has another mandatory parameter (song name) and one optional parameter (additional info).

The lyrics are written inside either ```songverse``` or ```songchorus``` environments that handle the spacing of the text. For repeatable parts there is the ```repeatable``` environment.

When a song is defined, it can be added to ```main.tex``` by calling the "song command", in this example case ```\jarjestoasiantuntija{\songnumber}```. The ```\songnumber``` is counter for the songs. For a custom song number, replace ```\songnumber``` with whatever you want, e.g n.

## Known issues

- Currently there's an issue with song headers being left dangling alone in the previous page sometimes. Probably best to just add pagebreaks when building the final version.
- Alphabetical ordering of the table of contents is a _pain_. The ```latexmkrc``` file contains a hacky script that handles the sorting, but it only works by first compiling with the second line commented out and then compiling again without the comment.
