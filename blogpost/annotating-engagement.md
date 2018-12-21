# Engaging Annotations or Annotating Engagement?

> Experiencing the metrics hype first hand

This year's President's Dream Colloquium on [**_Making Public Knowledge_**](https://www.sfu.ca/dean-gradstudies/events/dreamcolloquium/DreamColloquium-making-knowledge-public.html) at SFU was all about the public aspects of knowledge production and dissemination at universities. Fittingly, I found myself reading and creating public annotations for the course readings using a tool called [_Hypothesis_](https://hypothes.is/). One of the main features that Hypothesis offers is the public annotation of PDF files hosted online including the option **to view and reply to other users comments and highlights**. This fundamentally changes the nature of _doing the weekly readings_: The solitary task of understanding the ideas of the author is enhanced (or maybe drowned?) by the incessant chatter of fellow students' thoughts.

As a student, I really enjoyed this new form of _social reading_ powered by the internet and modern technology. Other students were adding definitions and clarifications around jargon, linking to relevant material outside of the academy, pointing to updates and revisions of studies, and also adding their own thoughts. It is not hard to see that this can be incredibly valuable as an educational method ([Hypothesis recently announced](https://web.hypothes.is/blog/hypothesis-launches-lms-app/) cooperations with several big learning platforms, e.g., Canvas or Moodle).

As a data scientist, I was immediately excited as I knew that Hypothesis provides an API to access the data underlying all annotations through code. E.g., one of the first things that I immediately wanted to see was the time that annotations were created relative to the next upcoming class with the expectation to see some serious last-minute (or maybe last-hour, or last-day?) activity. More about this a bit later in this text, but for now I would like to address the two kinds of questions that I wanted to ask:

1. **What do annotations say about their creators?**

    While the benefit of _social reading_ for the student was fairly obvious to me (an insight that I will revisit later on), I wanted to explore the stories that the data told _about_ the student. In an age of quantification and measurement, what does it mean to create public knowledge in the forms of online annotations? Can we and should we use this data to evaluate students?

2. **What do annotations say about the original content?**
   
   Academia is a place of tough competition. _Publish or perish_ basically summarises the environment that scientists and scholars are facing, as the available job positions are scarce while their assessment is based on mostly quantitative criteria such as publication volumne or terrible indicators such as the h-index or Journal Impact Factor (JIF). As a researcher in this field, I also wanted to explore meaning of annotation data for the author of the original paper.

![](two_areas.png)

Before we continue to talk about these two different questions, let's quickly get an overview of the actual data that we will use.

## Data and Code

First things first, all the code used to collect data, run analyses, and create plots is available and reusable in a public [GitHub repository](https://github.com/Bubblbu/public-knowledge-annotations).

Furthermore, I want to clarify at this point that this undertaking is by no means a rigorous, scientific study of the topic. What began as a few plots out of curiousity turned into a slightly more detailed exploration of the annotation data for a course that I attended. Hence, I would love to hear about your thoughts and other ideas for further analyses. Feel free to submit a [new issue](https://github.com/Bubblbu/public-knowledge-annotations/issues/new) or simply shoot me a text at [asura.enkhbayar@gmail.com](mailto:asura.enkhbayar@gmail.com).

---

The course [Making Knowledge Public](http://www.scholcommlab.ca/publicknowledgecourse/) took place over the course of _12 weeks_ with _9 different lecturers_ and _28 readings_ consisting of published articles, presentation slides, and chapters from books. The course was structured into four parts (including two introductory classes) with varying number of readings for each week.

Using the Hypothesis API, I found 1431 annotations for these 28 URLs. 24 of these 1431 annotations were created before our first class. Of the remaining 1417 annotations that were created during the 12 weeks, 1286 (91%) were created by students of this course.

|   Week | Date       | Title                                                           |   Part | Speaker            |   # of readings |   # of comments |
|-------:|:-----------|:----------------------------------------------------------------|-------:|:-------------------|----------------:|----------------:|
|      1 | 2018-09-06 | Introduction: Defining the public’s right to know               |      0 | Juan Pablo Alperin |               1 |               3 |
|      2 | 2018-09-13 | Calling Bullshit on Fake News                                   |      0 | Jevin West         |               3 |             177 |
|      3 | 2018-09-20 | Value of research in public policy                              |      1 | Nancy Olewiler     |               6 |             153 |
|      4 | 2018-10-01 | Knowledge Sharing and Social Responsibility                     |      1 | Mario Pinto        |               0 |               0 |
|      5 | 2018-10-04 | University-Community Connections                                |      2 | Luke Terra         |               3 |             264 |
|      6 | 2018-10-10 | Collaborating with indigenous communities in research           |      2 | John Borrows       |               1 |             108 |
|      7 | 2018-10-16 | Understanding the public’s use of research through social media |      2 | Juan Pablo Alperin |               1 |              90 |
|      8 | 2018-10-25 | Citizen Science                                                 |      2 | Shannon Dosemagen  |               3 |              98 |
|      9 | 2018-11-01 | Why access matters                                              |      3 | Juan Pablo Alperin |               3 |             162 |
|     10 | 2018-11-08 | Global participation in knowledge production                    |      3 | Hebe Vesuri        |               2 |             104 |
|     11 | 2018-11-15 | Critical Approaches to Open Access                              |      3 | Juan Pablo Alperin |               3 |             144 |
|     12 | 2018-11-22 | The Future of the Public Mission of Universities                |      3 | Robin DeRosa       |               2 |             128 |

Furthermore, Hypothesis provides some metadata for each of the annotations. The full reference for their API can be found [here](https://h.readthedocs.io/en/latest/api-reference/) but some of the metadata that might be relevant for us are:

- _username_ of author: This has been used to identify the comments created by students of this course
- _created_ and _updated_ timestamps: As annotations can be edited Hypothesis provides dates for the original creation and the last update.
- _text_: The actual content of the annotation (if available; annotations can be comments and highlights)
- _references_ to other comments: If the comment was a reply to another comment, this field would specify the ID of the original annotation
- _tags_: Authors can add tags or keywords to their comments. 

By combining the information from the course schedule with the annotation data using the students' Hypothesis usernames we can now start to explore the two questions we defined earlier.

## 1. What can we learn about the students of this course?

The one question that led to this blog post: When do students annotate papers? Figure 1 visualises the unsurprising fact that human beings (and students) work towards deadlines. The size of bubbles representing new comments on the readings increase in their size once the weekly lectures (red lines) approach.

![Overview of comments during the PDC](../plots/week_overview.png)

<p><em>Fig.1: Overview of comments during the PDC.</em></p>

We can depict this circumstance in an even more convincing way if we look at the days until the relevant class for each annotation. We would expect to see majority of the activity within the week before each class, especially peaking just before the final day. This is exactly what we observe in figure 2, which shows that more than 65% of all annotations are created on the same day as the class or the day before.

![days before class](../plots/days_before_class.png)
<p><em>Fig.2: Number of days before a class took place</em></p>

These findings are not surprising. The graph in figure 2 is cropped at day 1, as there was a tiny fraction of comments created after the day of the class. Out of the 1286 comments only 6 were created after the day of the lecture.

Now that we know when students annotate their readings, we can start to look at which readings were annotated more often than others. Figure 3 shows that the number of comments fluctuated around 100 comments per week with the exception of week 5 (Luke Terra's lecture on _University-Community Connections_).

![Comments per reading stacker per week](../plots/comments_per_reading.png)
<p><em>Fig.3: Each stacked sub-bar represents one reading. Multiple readings in the same week are stacked to represent the total of the week. Colors are according to the assigned part in the syllabus.</em></p>

Looking at this chart with the nice colorful bars, it is quite easy to conclude that week 5 was the most engaging one. A lot of students annotated the particular readings, with one of them accumulating as many as the aggregated readings did in other weeks which should be good, right? Or maybe not? At this point, we could eventually start to think about the _meaning of annotations_. Or, instead, following the tradition of certain scholarly institutions, we could simply keep counting more things!

An obvious next metric to try, given that we have the texts in our data, is the length of comments. Let's see if the median length of comments tells a different story about the individual weeks.

![Median length of comments per week](../plots/med_comment_length.png)
<p><em>Fig.4: Median length of comments for each week in characters. We can no longer plot the individual readings within each week, as the median length for the week is not the sum of the medians for each reading.</em></p>

When it comes to the longest comments, week 7 is ahead of the rest, while the majority of comments seem to be around 125 characters long. Combining these two metrics we can look at the weeks and individual readings as presented in the next figure.

![Median length of comments vs number of comments](../plots/comments_vs_length.png)
<p><em>Fig.5: Comparing the median length of comments with the number of comments for each part, week, and reading.</em></p>

- If we look at the weeks, we can see that there seems to be one major cluster with a similar number of comments with similar lengths. With the exception of week 1 (introduction) and 5 and 7, which we identified in the previous two plots, all weeks seem to have around 125 comments with a median length of 130 characters.
- Looking at individual articles that were read throughout the course, we get a slightly less clear picture. Looking at the scatterplot B in figure 5, I would suggest that the number of comments has a mild positive correlation with the length of comments.

### Zooming



But what about comment lengths and comment frequency for individual users? Can we model different _annotation styles_ based on these two variables?

![number of comments vs median length of comments](../plots/user_ranks_length_vs_comments.png)
<p><em>Fig.5: The changes of user rankings according to the number of comments created and the median length of comments</em></p>

Interestingly, for our limited dataset, there seem to be a few different types of annotaters in our class.

- _High frequency, short texts_: `anastasiak`, `mawaters`
- _Low frequency, long texts_: `Bubblbu`, `camilleweinsheimer`, `melissa_roach` 
- _Mid-high frequency, mid-long texts_: `aliceLF`, `KariGustafson`, `michelle_la`
- _Mid-low frequency, mid-short texts_: `carina.albrecht`, `cypriine`, `CSG`, `vreichsh`

`juan` was excluded as it was the Hypothesis account of our course instructor and `kprosser` due to the fact that they only created a single annoation.

### A few more possibilities

Just a few extras to show off other possible analyses based on the available data.

Figure 6 shows how the creation and update times contained in the annotations could be used to (very) roughly estimate the reading time for an article. Some obvious problems are work sessions spread across long timespans and that the actual activity of reading and thinking does not necessarily occur linearly.

![reading times](../plots/reading_times.png)
<p><em>Fig.6: Median reading times per article</em></p>

While reading comments I thought that linking to other resources (e.g., Wikipedia for definitions, follow-up research, or relevant news coverage) represented a special kind of annotation that felt more _engaging_. I was curious to see how frequent these comments with links to resources were in the data. Turns out that only 106 (8.2%) of all comments contained a URL. Figure 6 shows a breakdown of the most avid linkers among our group.

![comments containing URLs](../plots/comments_with_urls.png)
<p><em>Fig.6: Number of comments containing URLs</em></p>

## 2. Predicting engagement with annotations


9 students filled out the [survey](../data/survey.csv), while 7 provided a complete set of answers.

At this point, it is interesting to note that that week also received the most votes for the _most engaging_ week (3 votes ahead of Robin DeRosa with 2 votes).

Finally, I wanted to present a very quick and dirty attempt to quantify the predictability of _engagement_ of the parts, weeks, and readings in the syllabus. The survey results for these three categories were used as target variables which were to be predicted by the number of comments and median length of comments for individual users.

The, obviously naive, hypothesis is that _highly engaging_ readings (or weeks or parts) will evoke more or respectively longer annotations.

The following graph shows the difference in the rank between the user's actual _most engaging_ paper/week/part as reported in the survey and rank of the same reported paper/week/part as measured by number/length of comments. This means, that ideally we would see two matrices of 1s meaning that each self-reported item also took the 1st place in the measured ranking.

![predicting engagement](../plots/engagement_predictors.png)
<p><em>Fig.7: Differences between the rank of self-reported most-engaging items (rank: 1) and the ranks of items as measured by number and length of comments.</em></p>