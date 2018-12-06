# [MKP] - Hypothesis, Annotations, and Engagement

> An Exploration of public annotiations made during the #publicknowledge course during the Fall term 19' at SFU

Author: Asura Enkhbayar
Date: 05.12.2018

## Materials

- Full Jupyter notebook including code for analysis and plots: [notebook](code/results.ipynb)
- Presentation used for the last class of the course: [link](http://htmlpreview.github.io/?https://github.com/Bubblbu/public-knowledge-annotations/blob/master/code/presentation.html)
- Detailed survey results: [spreadsheet](https://docs.google.com/spreadsheets/d/1E6pEg0XN_D23kmaWL4wkbIysw6DHWdXmiNVY4cp4I18/edit?usp=sharing)
- About Hypothesis: [homepage](hypothes.is)

## The Data

The data used for this analysis comes from three different sources.

### 1. Making Knowledge Public - Course Material

The course structure and outline as described on the [syllabus](scholcommlab.ca/publicknowledge) has been manually saved in spreadsheets.

### 2. Survey among students

A survey among students was used to (1) identify and confirm Hypothesis usernames needed to differentiate comments relevant to the course and annotations created by other public users.

### 3. Our annotations retrieved from Hypothesis API

Hypothesis provides an API to programmatically retrieve annotation data for individual URLs. The URLs to the readings were available in the course material. The API returns the total number of annotations for each URL and a list of annotation object. Each annotation contains among other things:

- A unique ID for this annotation
- Date created
- Date updated
- The full text of the comment
- References (other annotations that this object was a reply to)
- The username of the author

## Some insights and results

![overview of comments during the PDC](plots/week_overview.png)

![days before class](plots/days_before_class.png)

![Comments per reading stacker per week](plots/comments_per_reading.png)

![Median length of comments vs number of comments](plots/comments_vs_length.png)

![number of comments vs median length of comments](plots/user_ranks_length_vs_comments.png)

![predicting engagement](plots/engagement_predictors.png)

![reading times](plots/reading_times.png)

![comments containing URLs](plots/comments_with_urls.png)

## Other Questions

- Interaction with other users

## Contact

I would love to hear about your thoughts and other ideas for further analyses. Feel free to submit an issue in this repository or simply shoot me a text at [asura.enkhbayar@gmail.com](mailto:asura.enkhbayar@gmail.com).

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.