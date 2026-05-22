# 1. Overview


## Objective

Create a process to convert YouTube transcription of auto-generated subtitles
into a human readable text.

## Problem

We need to guarantee that the original YT transcript content will not be summarized or edited by AI,
it must be literally what the human author produced, but turning a non human readable text into
a fully formated human readable text.

## Functional Requirements

- First of all the AI must read this Spec.md for guiding it during the whole process!

- After reading this Spec, the AI must ask: "Hi, there! Please, paste the YT transcription content now!"

- After receiving the content, AI must ask: "Received your content. Please, into which language do you want to translate it?"

- After receiving the desired target language, the AI must translate it (or keep it if the target language is
already the source language), but cannot ever change the content. It must be exactly the source text just formated
into a human redable final text version. 

- After the conclusion, AI must still consider this Spec.md and say: "Your content sent was done. Please, do you
have more content to be formated?". The cycle must then restart if the user send new content. However, the user may
receive as options: /send a new content (to reinitialize the process) or /finish (to quit the process, AI must say: "Thank you for trusting me as your pal for formating human transcription! See you next time!").

## Technical Requirements

The own LLM webchat interface.




