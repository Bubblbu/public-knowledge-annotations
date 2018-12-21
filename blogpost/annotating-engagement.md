# Engaging Annotations or Annotating Engagement?

> Exploring annotations as the metric of the classroom

21.12.2018, Asura Enkhbayar

---

This year's President's Dream Colloquium on [**_Making Public Knowledge_**](https://www.sfu.ca/dean-gradstudies/events/dreamcolloquium/DreamColloquium-making-knowledge-public.html) at SFU was all about the public aspects of knowledge production and dissemination at universities. Fittingly, I found myself reading and creating public annotations on the readings for the course using a tool called [_Hypothesis_](https://hypothes.is/). One of the main features that Hypothesis offers is the public annotation of PDFs including the option **to view and reply to other users comments and highlights**. This fundamentally changes the nature of working on the weekly readings: The solitary task of understanding a wall of text is enriched (or maybe drowned?) by the incessant chatter of fellow students' comments.

As a student, I really enjoyed this form of _social reading_ powered by the internet and technology. Other students were adding definitions and clarifications around jargon, linking to relevant material outside of the academy, pointing to updates and revisions of studies, and also adding their own thoughts. It is not hard to see that annotations can be incredibly valuable as an educational tool ([Hypothesis recently announced](https://web.hypothes.is/blog/hypothesis-launches-lms-app/) cooperations with several big learning platforms, e.g., Canvas or Moodle).

As a data scientist, I was quite excited about the fact that Hypothesis provides an API (application programming interface) to access the data underlying all annotations with code. E.g., I immediately wanted to see how early annotations were created relative to the next upcoming class, with the expectation to see some serious last-minute (or maybe last-hour, or last-day?) activity. More about this later on, but for now I would like to introduce the two big questions that I chose to investigate:

1. **What do annotations say about their creators?**

    While the benefits of _social reading_ for the student was fairly obvious to me, I wanted to explore what kind of story the data would tell about the student. In an age of quantification and measurement, what does it mean to create public knowledge in the forms of online annotations? Can we use this data to evaluate students and their performance? Should we?

2. **What do annotations say about the original content?**
   
   Academia is a world of competition. _Publish or perish_ wonderfully summarises the environment that scientists and scholars are facing, as available job positions are scarce while their applications are assessed based on criteria such as publication volume or terrible indicators such as the h-index<sup>[1](#hindex)</sup> or Journal Impact Factor<sup>[2](#jif)</sup> (JIF). Can we use annotation data to assess the articles? Does annotation behaviour reflect the engagement with the articles?

![](two_areas.png)

Before we continue to talk about these two different questions, let's quickly get an overview of the actual data that we will use.

## Data and Code

First things first, all the code used to collect data, run analyses, and create plots is available and reusable in a public [GitHub repository](https://github.com/Bubblbu/public-knowledge-annotations).

Furthermore, I want to clarify at this point that this undertaking is by no means a rigorous, scientific study of the topic. What began as a few curious plots turned into a slightly more detailed exploration of the annotation data for a course I attended. Hence, I would love to hear about your thoughts and other ideas for further directions and research. Feel free to submit a [new issue](https://github.com/Bubblbu/public-knowledge-annotations/issues/new) or simply shoot me a text at [asura.enkhbayar@gmail.com](mailto:asura.enkhbayar@gmail.com).

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

The initial question that led to this blog post: When do students annotate papers? Figure 1 visualises the unsurprising fact that human beings (and students) work towards deadlines. The size of bubbles representing new comments on the readings increase in their size as the weekly lectures (red lines) approach.

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

### Zooming in onto the students

After looking at the number of comments, length of comments, and their distribution across parts, weeks, and individual articles, we could now do similar analyses for individuals as we have each students Hypothesis accounts and the related comments.

I think that this dimension is especially interesting, as evaluation is a fundamental part of any _traditional_ education system. At this point, I simply want to emphasise that the availability of this kind of data will definitely be noticed, especially considering that _social reading_ and online annotations have made their move into the learning and teaching sector.

This topic will definitely require the attention of students and teachers, scholars and practitioners of pedagogy, and the general public. For now, I will stick to my knitting and present an example how the present data could be used to categorize different types of _annotation behaviour_.

The following plot shows the change in the rank of students measured by their number of annotations and median length of comments. I will use my own account as an example to elaborate:

My Hypothesis username is `Bubblbu`. Over the course of the 12 weeks I created 67 comments which puts me in a mid-lower place in the rankings. If we now look at the median length of my comments, we can see that with 268 characters I am in the second place.

![number of comments vs median length of comments](../plots/user_ranks_length_vs_comments.png)
<p><em>Fig.6: The changes of user rankings according to the number of comments created and the median length of comments</em></p>

Interestingly, looking at the overall annotation behaviour along these two dimensions, four different clusters of students<sup>[3](#excluded)</sup> emerge:

- High frequency; short texts: `anastasiak`, `mawaters`
- High frequency; long texts: `aliceLF`, `KariGustafson`, `michelle_la`
- Low frequency; long texts: `Bubblbu`, `camilleweinsheimer`, `melissa_roach` 
- Low frequency; short texts: `carina.albrecht`, `cypriine`, `CSG`, `vreichsh`

Students that created the most annotations also created the shortest comments and vice versa. For those students that did not end up in the extremes, we can still observe the same negative relationship between frequency and length of annotations.

But what does that mean? Should one of these groups be rewarded with a better grade than another one? Should students be rewarded for the volume of their annotations, longer and exhaustive comments, or should it be a composite score? But what if students start to game the system and optimise towards the best grade? ...

For those of you who are familiar with *metrics research in other scholarly domains, these questions will be reminiscent of the story how the current [business of scholarship](https://paywallthemovie.com/) emerged; namely out of the effort to create better indicators for research quality a.k.a. [excellence](https://www.youtube.com/watch?v=SLst9X6A6OE).

I am aware that I just made a pretty big jump from grading students to the fundamental challenges of scholarship in the 21st century, but I believe that any attempt to measure scholarly outputs by the means of reduction to numbers should be critically questioned.

### Some more possible number games

Two more examples for metrics that we can extract from the data.

Figure 7 shows how the creation and update times contained in the annotations could be used to (very) roughly estimate the reading time for an article. Some obvious issues arise if students annotate across several reading sessions spread across longer timespans. Overall, this method of approximating the actual reading time of an article is quite poor but, as the h-index shows, sometimes the quality of a measure does not really matter. ¯\_(ツ)_/¯

![reading times](../plots/reading_times.png)
<p><em>Fig.7: Median reading times per article</em></p>

While working on the course readings, I really liked when links to external resources (e.g., Wikipedia for definitions, follow-up research, or relevant news coverage) were provided. I am not sure if anyone has already created an ontology of annotations, but these outlinks definitely represent a fundamentally different type of commenting. I was curious to see how often comments contained URLs. Turns out that only 106 (8.2%) of all comments contained one in our dataset. Figure 8 shows a breakdown of the most avid linkers among our group.

![comments containing URLs](../plots/comments_with_urls.png)
<p><em>Fig.8: Number of comments containing URLs</em></p>

## 2. What can we learn about the authors of the course readings?

So far, I have proudly donned my hat as a quantitative researcher and attempted to explore the data at hand and provide a few simple, but hopefully interesting, insights. In order to answer the next question, I decided to up my game as a student in an interdisciplinary program, and did what every data scientist with a love for the qualitative does: Send out a survey.

Specifically, I sent out a survey to my fellow students to find out about their experience with Hypothesis, their reading and annotating habits, and, most importantly, which part, week, and reading they found most _"engaging"_. Fully aware of the danger zone that I was entering by trying to measure a concept like _engagement_, I tried to fully embrace the ambiguity. From the survey:

> "I am broadly defining engagement as a form of interaction. E.g., a particularly engaging paper is interesting, might bring forth additional questions, cause new insights, lead to new ideas and connections, etc... 

In addition to nominating the "_most engaging_" week, part, and reading the participants were asked to give a reason why they gave their particular answer.

9 students filled out the survey out of which 7 provided a complete set of answers. The results are publicly available in the GitHub repository (CSV [here](../data/survey.csv)). Unfortunately, I had no time to create plots for all questions in the complete survey (which can be found here: [PDF](../data/survey_questions.pdf)).

### Matching engagement with annotations

I want to present a playful attempt at quantifing the predictability of the _engagement_ for parts, weeks, and readings in the syllabus. The survey results for these three categories were used as target variables which were to be predicted by the number of comments and median length of comments for individual users.

The, obviously naive, hypothesis is that _highly engaging_ readings (or weeks or parts) will either evoke more annotations or longer comments. For a particular user that would mean that the paper that has received the most comments (or the longest ones) should also be reported as the "most engaging" one. As my survey did not ask for a particular ranking of engagement for every single article, we will simply compare the rank of the nominated, most engaging paper with the rank it takes in each students ranking in terms of the number of comments.

The following graph shows the difference in the rank between the user's actual _most engaging_ paper/week/part as reported in the survey and rank of the same reported paper/week/part as measured by number/length of comments. In the example of the user `carina.albrecht` we can see that the paper she reported as "most engaging" ranked 4th in terms of the number comments. Interestingly, the same paper is ranked as the "most engaging" one if measured by the length of comments.

![predicting engagement](../plots/engagement_predictors.png)
<p><em>Fig.7: Differences between the rank of self-reported most-engaging items (rank: 1) and the ranks of items as measured by number and length of comments.</em></p>

The lower the numbers in those two matrices are, the better are the measures as predictors of "engagement". Once again, I will not attempt to provide any concrete numbers as I want to emphasise that these examples are closer to anecdotal evidence than a scientific study. Furthermore, in the face of the limitations of the data (and method) I will not attempt to mislead anyone with terms such as accuracy or precision.

Bottom line, I am not surprised to see that the ranking of readings by either frequency or length of comments aligns with the self-reported "most engaging" papers for some cases. After presenting intermediate results to my classmates we quickly realised that (1) the understanding of _engaging papers_ and (2) the purpose of annotations differed between us. While some thought that an engaging paper would be interesting, others were eventually looking for provoking and opposing opinions. Similarly, annotations were used as markers of support or disagreement, "likes", or flags for personal research.

These, admittedly very quick and dirty, results are to be taken as an example for the possibilities that are enabled by the special circumstances of using Hypothesis in the classroom. While my survey was thrown together quite quickly and is limited to 7 students, I would be quite interested in similar studies conducted with other classes, reading groups, or journal clubs.

## Conclusion

Reading articles _with_ your classmates using Hypothesis was a really fun and, more importantly, insightful experience. I found out that sometimes I prefer to read texts without any annotations in order retain the factors of novelty and discovery. Then, at other times, I found the thoughts and links left by fellow students incredibly helpful and thought-provoking. Hypothesis in the classroom is fundamentally changing how students interact with each other and their texts.

Nevertheless, in this blogpost I decided to explore a completely different side to the story. I wanted to look at the available information through the eyes of a data scientist and scientometrician and try to play the "indicator game". While exploration, predicting variables, and evaluating the available data is incredibly fun and can be equally useful, it became clear that many of the bigger questions would not be answered by counting more things.

This case study of a tiny classroom at SFU was a great exercise myself as a student, but knowing that _social reading_ and web annotations are inevitably going to arrive at the academy, I am asking myself if and how some of the issues raised in this blog post will be addressed in the near future.

Annotations have already found their way into the science evaluation universe (e.g., CrossRef is providing data about public annotations on scholarly documents through their [Event Data](https://www.crossref.org/services/event-data/) service). While I am excited about the possibilities and developments in that realm, I am asking myself how this technology will influence education and student evaluation.

## Footnotes

<a name="hindex">1</a>: The h-index, or the academic equivalent of the stag's antlers ([https://www.theguardian.com/commentisfree/2012/jan/06/bad-science-h-index](https://www.theguardian.com/commentisfree/2012/jan/06/bad-science-h-index))
<a name="jif">2</a>: The Impact Factor and Its Discontents: Reading list on controversies and shortcomings of the Journal Impact Factor. ([http://blogs.lse.ac.uk/impactofsocialsciences/2014/07/30/reading-list-on-the-journal-impact-factor/](http://blogs.lse.ac.uk/impactofsocialsciences/2014/07/30/reading-list-on-the-journal-impact-factor/))
<a name="excluded">3</a>: `juan` was excluded as this is the username of our course instructor and `kprosser` due to the fact that they only created a single annoation.