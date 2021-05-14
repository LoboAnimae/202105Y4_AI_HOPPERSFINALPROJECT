# Hoppers Deep Reinforcement AI

## Metadata

---

    Universidad del Valle de Guatemala
    Andrés Quan-Littow      17652
    Artificial Intelligence
    4th Year, 1st Semester
    2021

    The code in this repository is open source and free to use to your liking. 
    It was used to complete a project with Deep Reinforcement Learning. 

## Project Description

---

Project developed using TensorFlow 2.0 with Keras to play "Hoppers"

Hoppers is a game that looks and plays like chinese checkers.


## How the AI Will Communicate with the World

---
The AI uses the following XML to communicate with the world:

    <move>
      <from row="1" col="8"/>
      <to row="8" col="7"/>
      <path>
        <pos row="1" col="8"/>
        <pos row="3" col="8"/>
        ...
        <pos row="8" col="7"/>
      </path>
    </move>