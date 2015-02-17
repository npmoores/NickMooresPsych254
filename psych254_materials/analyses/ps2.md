---
title: 'Psych 254 W15 PS #2'
author: "Nicholas Moores"
date: "February 4, 2015"
output: html_document
---

This is problem set #2, in which we hope you will practice the visualization package ggplot2, as well as hone your knowledge of the packages tidyr and dplyr. 

Part 1: Basic intro to ggplot
=============================

Part 1A: Exploring ggplot2 using qplot
--------------------------------------

Note, that this example is from the_grammar.R on http://had.co.nz/ggplot2 
I've adapted this for psych 254 purposes

First install and load the package.


```r
library(ggplot2)
library(dplyr)
```

```
## 
## Attaching package: 'dplyr'
## 
## The following object is masked from 'package:stats':
## 
##     filter
## 
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

```r
library(tidyr)
library(stringr)
```

Now we're going to use qplot. qplot is the easy interface, meant to replace plot. You can give it simple `qplot(x,y)` examples, or slightly more complex examples like `qplot(x, y, col=grp, data=d)`. 

We're going to be using the diamonds dataset. This is a set of measurements of diamonds, along with their price etc.


```r
head(diamonds)
```

```
##   carat       cut color clarity depth table price    x    y    z
## 1  0.23     Ideal     E     SI2  61.5    55   326 3.95 3.98 2.43
## 2  0.21   Premium     E     SI1  59.8    61   326 3.89 3.84 2.31
## 3  0.23      Good     E     VS1  56.9    65   327 4.05 4.07 2.31
## 4  0.29   Premium     I     VS2  62.4    58   334 4.20 4.23 2.63
## 5  0.31      Good     J     SI2  63.3    58   335 4.34 4.35 2.75
## 6  0.24 Very Good     J    VVS2  62.8    57   336 3.94 3.96 2.48
```

```r
qplot(diamonds$carat, diamonds$price)
```

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-2-1.png) 

Scatter plots are trivial, and easy to add features to. Modify this plot so that it uses the dataframe rather than working from variables in the general namespace (good to get away from retyping `diamonds$` every time you reference a variable). 


```r
qplot(carat, price, data=diamonds, geom='point') +
  ggtitle("Diamonds by Carat and Price") +
  xlab("Diamond Carats") + ylab("Diamond Price")
```

![plot of chunk unnamed-chunk-3](figure/unnamed-chunk-3-1.png) 

Try adding clarity and cut, using shape and color as your visual variables. 


```r
qplot(carat, price, data=diamonds, geom='point', shape=clarity, color=cut) +
  ggtitle("Diamonds by Carat and Price") +
  xlab("Diamond Carats") + ylab("Diamond Price")
```

```
## Warning: The shape palette can deal with a maximum of 6 discrete values
## because more than 6 becomes difficult to discriminate; you have 8.
## Consider specifying shapes manually. if you must have them.
```

```
## Warning: Removed 5445 rows containing missing values (geom_point).
```

```
## Warning: The shape palette can deal with a maximum of 6 discrete values
## because more than 6 becomes difficult to discriminate; you have 8.
## Consider specifying shapes manually. if you must have them.
```

![plot of chunk unnamed-chunk-4](figure/unnamed-chunk-4-1.png) 
One of the primary benefits of `ggplot2` is the use of facets - also known as small multiples in the Tufte vocabulary. That last plot was probably hard to read. Facets could make it better. Try adding a `facets = x ~ y` argument. `x ~ y` means row facets are by x, column facets by y. 


```r
qplot(carat, price, data=diamonds, geom='point', shape=clarity, color=cut,
  facets = color ~ cut,
  main="Diamonds by Carat and Price",
  xlab="Diamond Carats", ylab="Diamond Price")
```

```
## Warning: The shape palette can deal with a maximum of 6 discrete values
## because more than 6 becomes difficult to discriminate; you have 8.
## Consider specifying shapes manually. if you must have them.
```

```
## Warning: Removed 6 rows containing missing values (geom_point).
```

```
## Warning: Removed 22 rows containing missing values (geom_point).
```

```
## Warning: Removed 75 rows containing missing values (geom_point).
```

```
## Warning: Removed 50 rows containing missing values (geom_point).
```

```
## Warning: Removed 172 rows containing missing values (geom_point).
```

```
## Warning: Removed 3 rows containing missing values (geom_point).
```

```
## Warning: Removed 52 rows containing missing values (geom_point).
```

```
## Warning: Removed 213 rows containing missing values (geom_point).
```

```
## Warning: Removed 132 rows containing missing values (geom_point).
```

```
## Warning: Removed 414 rows containing missing values (geom_point).
```

```
## Warning: Removed 9 rows containing missing values (geom_point).
```

```
## Warning: Removed 50 rows containing missing values (geom_point).
```

```
## Warning: Removed 241 rows containing missing values (geom_point).
```

```
## Warning: Removed 111 rows containing missing values (geom_point).
```

```
## Warning: Removed 708 rows containing missing values (geom_point).
```

```
## Warning: Removed 5 rows containing missing values (geom_point).
```

```
## Warning: Removed 63 rows containing missing values (geom_point).
```

```
## Warning: Removed 269 rows containing missing values (geom_point).
```

```
## Warning: Removed 258 rows containing missing values (geom_point).
```

```
## Warning: Removed 1085 rows containing missing values (geom_point).
```

```
## Warning: Removed 1 rows containing missing values (geom_point).
```

```
## Warning: Removed 35 rows containing missing values (geom_point).
```

```
## Warning: Removed 144 rows containing missing values (geom_point).
```

```
## Warning: Removed 152 rows containing missing values (geom_point).
```

```
## Warning: Removed 552 rows containing missing values (geom_point).
```

```
## Warning: Removed 1 rows containing missing values (geom_point).
```

```
## Warning: Removed 28 rows containing missing values (geom_point).
```

```
## Warning: Removed 88 rows containing missing values (geom_point).
```

```
## Warning: Removed 107 rows containing missing values (geom_point).
```

```
## Warning: Removed 274 rows containing missing values (geom_point).
```

```
## Warning: Removed 1 rows containing missing values (geom_point).
```

```
## Warning: Removed 7 rows containing missing values (geom_point).
```

```
## Warning: Removed 27 rows containing missing values (geom_point).
```

```
## Warning: Removed 36 rows containing missing values (geom_point).
```

```
## Warning: Removed 54 rows containing missing values (geom_point).
```

```
## Warning: The shape palette can deal with a maximum of 6 discrete values
## because more than 6 becomes difficult to discriminate; you have 8.
## Consider specifying shapes manually. if you must have them.
```

![plot of chunk unnamed-chunk-5](figure/unnamed-chunk-5-1.png) 

But facets can also get overwhelming. Try to strike a good balance between color, shape, and faceting.

HINT: `facets = . ~ x` puts x on the columns, but `facets = ~ x` (no dot) *wraps* the facets. These are underlying calls to different functions, `facet_wrap` (no dot) and `facet_grid` (two arguments). 


```r
qplot(carat, price, data=diamonds, geom='point', shape=clarity, color=cut,
  facets = ~ cut,
  main="Diamonds by Carat and Price",
  xlab="Diamond Carats", ylab="Diamond Price")
```

```
## Warning: The shape palette can deal with a maximum of 6 discrete values
## because more than 6 becomes difficult to discriminate; you have 8.
## Consider specifying shapes manually. if you must have them.
```

```
## Warning: Removed 26 rows containing missing values (geom_point).
```

```
## Warning: Removed 257 rows containing missing values (geom_point).
```

```
## Warning: Removed 1057 rows containing missing values (geom_point).
```

```
## Warning: Removed 846 rows containing missing values (geom_point).
```

```
## Warning: Removed 3259 rows containing missing values (geom_point).
```

```
## Warning: The shape palette can deal with a maximum of 6 discrete values
## because more than 6 becomes difficult to discriminate; you have 8.
## Consider specifying shapes manually. if you must have them.
```

![plot of chunk unnamed-chunk-6](figure/unnamed-chunk-6-1.png) 

```r
qplot(carat, price, data=diamonds, geom='point', shape=clarity, color=cut,
  facets = . ~ cut,
  main="Diamonds by Carat and Price",
  xlab="Diamond Carats", ylab="Diamond Price")
```

```
## Warning: The shape palette can deal with a maximum of 6 discrete values
## because more than 6 becomes difficult to discriminate; you have 8.
## Consider specifying shapes manually. if you must have them.
```

```
## Warning: Removed 26 rows containing missing values (geom_point).
```

```
## Warning: Removed 257 rows containing missing values (geom_point).
```

```
## Warning: Removed 1057 rows containing missing values (geom_point).
```

```
## Warning: Removed 846 rows containing missing values (geom_point).
```

```
## Warning: Removed 3259 rows containing missing values (geom_point).
```

```
## Warning: The shape palette can deal with a maximum of 6 discrete values
## because more than 6 becomes difficult to discriminate; you have 8.
## Consider specifying shapes manually. if you must have them.
```

![plot of chunk unnamed-chunk-6](figure/unnamed-chunk-6-2.png) 

The basic unit of a ggplot plot is a "geom" - a mapping between data (via an "aesthetic") and a particular geometric configuration on coordinate axes. 

Let's try some other geoms and manipulate their parameters. First, try a histogram (`geom="hist"`). 


```r
qplot(x=price, data=diamonds, geom='histogram', binwidth=100,
  main="Diamonds by Carat and Price by Clarity and Cut",axis.text.x = element_text(angle = 45, hjust=1),
  xlab="Diamond Price", ylab="Frequency")
```

![plot of chunk unnamed-chunk-7](figure/unnamed-chunk-7-1.png) 

Now facet your histogram by clarity and cut. 


```r
qplot(x=price, data=diamonds, geom='histogram', facets = clarity ~ cut, binwidth=100,
  main="Frequency of Diamond Price by Clarity and Cut",axis.text.x = element_text(angle = 45, hjust=1),
  xlab="Diamond Price", ylab="Frequency")
```

![plot of chunk unnamed-chunk-8](figure/unnamed-chunk-8-1.png) 

I like a slightly cleaner look to my plots. Luckily, ggplot allows you to add "themes" to your plots. Try doing the same plot but adding `+ theme_bw()` or `+ theme_classic()`. Different themes work better for different applications, in my experience. 


```r
qplot(x=price, data=diamonds, geom='histogram', binwidth=100,
  facets = clarity ~ cut,axis.text.x = element_text(angle = 45, hjust=1),
  main="Frequency of Diamond Price by Clarity and Cut",
  xlab="Diamond Price", ylab="Frequency") + theme_bw()
```

![plot of chunk unnamed-chunk-9](figure/unnamed-chunk-9-1.png) 

Part 1B: Exploring ggplot2 using ggplot
---------------------------------------

`ggplot` is just a way of building `qplot` calls up more systematically. It's
sometimes easier to use and sometimes a bit more complicated. What I want to show off here is the functionality of being able to build up complex plots with multiple elements. You can actually do this using qplot pretty easily, but there are a few things that are hard to do. 

`ggplot` is the basic call, where you specify A) a dataframe and B) an aesthetic mapping from variables in the plot space to variables in the dataset. 


```r
d <- ggplot(diamonds, aes(x=carat, y=price)) # first you set the aesthetic and dataset
d + geom_point() # then you add geoms
```

![plot of chunk unnamed-chunk-10](figure/unnamed-chunk-10-1.png) 

```r
d + geom_point(aes(colour = carat)) # and you can keep doing this to add layers to the plot
```

![plot of chunk unnamed-chunk-10](figure/unnamed-chunk-10-2.png) 

Try writing this as a single set of additions (e.g. one line of R code, though you can put in linebreaks). This is the most common workflow for me. 



```r
d <- ggplot(diamonds, aes(x=carat, y=price)) + geom_point() + geom_point(aes(colour = carat)) # and you can keep doing this to add layers to the plot
d
```

![plot of chunk unnamed-chunk-11](figure/unnamed-chunk-11-1.png) 


You can also set the aesthetic separately for each geom, and make some great plots this way. Though this can get complicated. Try using `ggplot` to build a histogram of prices. 


```r
d <- ggplot(diamonds, aes(x=price)) + geom_histogram(binwidth=.5, colour="black", fill="white") +
geom_vline(aes(xintercept=mean(price, na.rm=T)),   # Ignore NA values for mean
               color="red", linetype="dashed", size=1)
d
```

![plot of chunk unnamed-chunk-12](figure/unnamed-chunk-12-1.png) 

Part 2: Diving into real data: Sklar et al. (2012)
==================================================

Sklar et al. (2012) claims evidence for unconscious arithmetic processing. We're going to do a reanalysis of their Experiment 6, which is the primary piece of evidence for that claim. The data are generously contributed by Asael Sklar. 

First let's set up a few preliminaries. 


```r
library(tidyr)
library(dplyr)
library(ggplot2)
sem <- function(x) {sd(x) / sqrt(length(x))}
ci95 <- function(x) {sem(x) * 1.96}
```

Data Prep
---------

First read in two data files and subject info. A and B refer to different trial order counterbalances. 


```r
subinfo <- read.csv("../data/sklar_expt6_subinfo_corrected.csv")
d.a <- read.csv("../data/sklar_expt6a_corrected.csv")
d.b <- read.csv("../data/sklar_expt6b_corrected.csv")
```

Gather these datasets into long form and get rid of the Xs in the headers.


```r
subinfo <- tbl_df(subinfo)
d.a <- tbl_df(d.a)
d.b <- tbl_df(d.b)
d.a.tidy <- d.a %>% gather("x_type", "RT", X1:X21, na.rm=TRUE) %>% mutate(x_type = gsub("X","",x_type))
d.b.tidy <- d.b %>% gather("x_type", "RT", X22:X42, na.rm=TRUE) %>% mutate(x_type = gsub("X","",x_type))
glimpse(subinfo)
```

```
## Observations: 42
## Variables:
## $ subid             (int) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1...
## $ presentation.time (int) 1700, 1700, 1700, 1700, 1700, 1700, 1700, 17...
## $ subjective.test   (int) 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1,...
## $ objective.test    (dbl) 0.5873016, 0.6406250, 0.5625000, 0.6111111, ...
```

```r
glimpse(d.a.tidy)
```

```
## Observations: 3120
## Variables:
## $ prime          (fctr) =1+2+5, =1+3+5, =1+4+3, =1+6+3, =1+9+2, =1+9+3...
## $ prime.result   (int) 8, 9, 8, 10, 12, 13, 12, 11, 12, 13, 10, 13, 9,...
## $ target         (int) 9, 11, 12, 12, 11, 12, 11, 10, 11, 9, 12, 11, 1...
## $ congruent      (fctr) no, no, no, no, no, no, no, no, no, no, no, no...
## $ operand        (fctr) A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A...
## $ distance       (int) -1, -2, -4, -2, 1, 1, 1, 1, 1, 4, -2, 2, -3, -1...
## $ counterbalance (int) 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,...
## $ x_type         (chr) "1", "1", "1", "1", "1", "1", "1", "1", "1", "1...
## $ RT             (int) 597, 699, 700, 628, 768, 595, 664, 803, 767, 70...
```

```r
glimpse(d.b.tidy)
```

```
## Observations: 3111
## Variables:
## $ prime          (fctr) =1+2+9, =1+3+6, =1+5+3, =1+6+2, =1+7+2, =2+3+5...
## $ prime.result   (int) 12, 10, 9, 9, 10, 10, 11, 12, 14, 11, 8, 9, 11,...
## $ target         (int) 8, 14, 12, 10, 11, 12, 10, 9, 13, 13, 9, 11, 13...
## $ congruent      (fctr) no, no, no, no, no, no, no, no, no, no, no, no...
## $ operand        (fctr) A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A...
## $ distance       (int) 4, -4, -3, -1, -1, -2, 1, 3, 1, -2, -1, -2, -2,...
## $ counterbalance (int) 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,...
## $ x_type         (chr) "22", "22", "22", "22", "22", "22", "22", "22",...
## $ RT             (int) 700, 559, 803, 628, 665, 701, 701, 628, 735, 73...
```

Bind these together. Check out `bind_rows`.


```r
d.all.tidy <- bind_rows(d.a.tidy, d.b.tidy)
```

Merge these with subject info. You will need to look into merge and its relatives, `left_join` and `right_join`. Call this dataframe `d`, by convention. 


```r
subinfo <- subinfo %>% rename(subjectID = subid)
d.all.tidy <- d.all.tidy %>% rename(subjectID = x_type)
subinfo$subjectID <- as.factor(subinfo$subjectID)
d.all.tidy$subjectID <- as.factor(d.all.tidy$subjectID)
d.all.tidy <- left_join(subinfo, d.all.tidy, by="subjectID")
```

```
## Warning: joining factors with different levels, coercing to character
## vector
```

```r
d.all.tidy$subjectID <- as.factor(d.all.tidy$subjectID)
```

Clean up the factor structure.


```r
d.all.tidy$presentation.time <- factor(d.all.tidy$presentation.time)
levels(d.all.tidy$operand) <- c("addition","subtraction")
```

Data Analysis Preliminaries
---------------------------

Operand x congruency x presentation time. Challenging to know what to collapse and what not to.

Examine the basic properties of the dataset. First, take a histogram.


```r
m.rt <- exp(mean(log(d.all.tidy$RT),na.rm=TRUE)) #take log average of RT: average natural logs of RTs, then take the exponential of that
sd.rt <- exp(sd(log(d.all.tidy$RT),na.rm=TRUE)) #geometric standard deviation: exponentiated value of the standard deviation of the log-transformed values
qplot(RT, data=d.all.tidy) + 
  geom_vline(xintercept=m.rt + 2*sd.rt, col="red", lty=2) + #lets us view how much is spread 2 SDs above mean
  geom_vline(xintercept=m.rt - 2*sd.rt, col="red", lty=2) + #lets us view how much is spread 2 SDs below mean
  xlab("RT spread") +
  ylab("Frequency") +
  ggtitle("RT Histogram of Sklav Data (marking +/- 2 SDs)")
```

```
## stat_bin: binwidth defaulted to range/30. Use 'binwidth = x' to adjust this.
```

![plot of chunk unnamed-chunk-19](figure/unnamed-chunk-19-1.png) 

Challenge question: what is the sample rate of the input device they are using to gather RTs?


```r
ggplot(d.all.tidy, aes(x=RT, y=congruent)) + geom_point()
```

![plot of chunk unnamed-chunk-20](figure/unnamed-chunk-20-1.png) 
The sampling rate seems to be about 30 samples per second!

Sklar et al. did two manipulation checks. Subjective - asking participants whether they saw the primes - and objective - asking them to report the parity of the primes (even or odd) to find out if they could actually read the primes when they tried. Examine both the unconscious and conscious manipulation checks (this information is stored in subinfo). What do you see? Are they related to one another?


```r
manipcheck <- glm(subjective.test ~ objective.test, d.all.tidy, family = binomial, na.action = na.omit)
print(summary(manipcheck))
```

```
## 
## Call:
## glm(formula = subjective.test ~ objective.test, family = binomial, 
##     data = d.all.tidy, na.action = na.omit)
## 
## Deviance Residuals: 
##     Min       1Q   Median       3Q      Max  
## -2.3827  -0.8239  -0.3895   0.6593   1.9773  
## 
## Coefficients:
##                Estimate Std. Error z value Pr(>|z|)    
## (Intercept)     -5.9395     0.1590  -37.37   <2e-16 ***
## objective.test   9.4567     0.2594   36.46   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## (Dispersion parameter for binomial family taken to be 1)
## 
##     Null deviance: 8638.0  on 6230  degrees of freedom
## Residual deviance: 6140.9  on 6229  degrees of freedom
## AIC: 6144.9
## 
## Number of Fisher Scoring iterations: 5
```

```r
ggplot(d.all.tidy, aes(x=objective.test, y=subjective.test)) + geom_point() +
  stat_smooth(method="glm", family="binomial", se=FALSE)
```

![plot of chunk unnamed-chunk-21](figure/unnamed-chunk-21-1.png) 
These two are indeed related to each other, as participants' score on the objective test is a significant predictor of their performance on the subjective test (beta=9.457, SE=0.26, z=36.46, p < 0.001). As their scores on the objective test increase they are more likely to perform correctly on the subjective test (they can't report the parity of the primes if they couldn't read the primes, for one).

OK, let's turn back to the measure and implement Sklar et al.'s exclusion criterion. You need to have said you couldn't see (subjective test) and also be not significantly above chance on the objective test (< .6 correct). Call your new data frame `ds`.


```r
ds <- d.all.tidy %>% filter((d.all.tidy$subjective.test==0) & (d.all.tidy$objective.test < .6))
ds <- tbl_df(ds)
```

Sklar et al.'s analysis
-----------------------

Sklar et al. show a plot of a "facilitation effect" - the time to respond to incongruent primes minus the time to respond to congruent primes. They then show plot this difference score for the subtraction condition and for the two presentation times they tested. Try to reproduce this analysis.

HINT: first take averages within subjects, then compute your error bars across participants, using the `sem` function (defined above). 
somewhere: do objective.test x facilitation scatterplot with lm

somewhere: do distance x RT scatterplot, with color by congruent

```r
plot.style <- theme(panel.grid.major=element_blank(), legend.position="right", plot.title=element_text(face="bold", size=14), axis.title=element_text(size=12))
PD <- position_dodge(.9)

ds_graph <- ds %>% filter((ds$presentation.time==1700) & (ds$operand=="subtraction"))
ds_graph <- select(ds_graph, one_of(c("subjectID","presentation.time","congruent","RT")))
ds_graphcon <- ds_graph %>% filter(ds_graph$congruent=="yes") %>% rename(yesRT=RT)
congruent_rts <- aggregate(yesRT ~ subjectID, ds_graphcon, mean)
ds_graphinc <- ds_graph %>% filter(ds_graph$congruent=="no") %>% rename(noRT=RT)
incongruent_rts <- aggregate(noRT ~ subjectID, ds_graphinc, mean)
ds_1700 <- left_join(congruent_rts, incongruent_rts, by="subjectID") %>% mutate(diff = abs(noRT-yesRT))
ds_1700 <- ds_1700 %>% mutate(presentation.time = 1700)
ds_1700 <- ds_1700 %>% mutate(meanDiff = mean(diff))

ds_graph <- ds %>% filter(ds$presentation.time==2000)
ds_graph <- select(ds_graph, one_of(c("subjectID","presentation.time","congruent","RT")))
ds_graphcon <- ds_graph %>% filter(ds_graph$congruent=="yes") %>% rename(yesRT=RT)
congruent_rts <- aggregate(yesRT ~ subjectID, ds_graphcon, mean)
ds_graphinc <- ds_graph %>% filter(ds_graph$congruent=="no") %>% rename(noRT=RT)
incongruent_rts <- aggregate(noRT ~ subjectID, ds_graphinc, mean)
ds_2000 <- left_join(congruent_rts, incongruent_rts, by="subjectID") %>% mutate(diff = abs(noRT-yesRT))
ds_2000 <- ds_2000 %>% mutate(presentation.time = 2000) %>% mutate(meanDiff = mean(diff))

ds_final <- bind_rows(ds_1700,ds_2000)
ds_final <- ds_final %>% mutate(sem = sem(meanDiff))
```

Now plot this summary, giving more or less the bar plot that Sklar et al. gave (though I would keep operation as a variable here. Make sure you get some error bars on there (e.g. `geom_errorbar` or `geom_linerange`). 


```r
qplot(presentation.time, meanDiff,
      geom="bar",
      position="dodge",
      stat="identity",
      data=ds_final) +
      geom_linerange(aes(ymin=diff-sem, ymax=diff+sem), colour="black", width=.2, position=PD) +
      xlab("Representation Duration") +
      ylab("Facilitation (mean)") +
      ggtitle("Facilitation Effect") + plot.style
```

![plot of chunk unnamed-chunk-24](figure/unnamed-chunk-24-1.png) 

What do you see here? How close is it to what Sklar et al. report? Do the error bars match? How do you interpret these data? 

The data do match what Sklar et al. report, but only when I took the absolute value of the difference between the average RT in the priming condition and the average RT in the control condition. I believe their claim rests upon the prime condition taking longer than the control condition, so the fact that this effect doesn't appear unless you look at the absolute value of the difference makes it very difficult to interpret these data. In addition, the error bars in Sklar's graph do not match mine because Sklar only shows half of one standard error of the mean on either side of the bar height. I could interpret these data to mean that when subjects have 2000 msec to view the stimulus, there is less difference in their reaction time between when they view congruent as opposed to incongruent primes. When the representation is only there for 1700 msec, however, the difference is much larger between congruent and incongruent primes, and the directionality of the difference is not consistent across subjects; the magnitude of the difference simply increases.

Challenge problem: verify Sklar et al.'s claim about the relationship between RT and the objective manipulation check.

To verify that there is no relationship between RT and the objective manipulation check, I first get a sense of the data by plotting first, all of the subjects, and then second, only the included subjects, with a regression line fitting the relationship between reaction time and performance on the objective test.

Finally I examine the linear model used to construct the graph of the relationship between reaction time and the objective manipulation test.

```r
ggplot(d.all.tidy, aes(x=RT, y=objective.test)) + geom_point() +
  stat_smooth(method="lm", se=FALSE)
```

![plot of chunk unnamed-chunk-25](figure/unnamed-chunk-25-1.png) 

```r
ggplot(ds, aes(x=RT, y=objective.test)) + geom_point() +
  stat_smooth(method="lm", se=FALSE)
```

![plot of chunk unnamed-chunk-25](figure/unnamed-chunk-25-2.png) 

```r
manipcheckcheck <- lm(objective.test ~ RT, ds, na.action = na.omit)
print(summary(manipcheckcheck))
```

```
## 
## Call:
## lm(formula = objective.test ~ RT, data = ds, na.action = na.omit)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.15176 -0.04048  0.02036  0.05144  0.08635 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 4.920e-01  6.216e-03  79.146   <2e-16 ***
## RT          1.828e-05  8.983e-06   2.035   0.0419 *  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.06417 on 2529 degrees of freedom
## Multiple R-squared:  0.001635,	Adjusted R-squared:  0.00124 
## F-statistic: 4.142 on 1 and 2529 DF,  p-value: 0.04193
```
As the lm() output above shows, even for the subjects who were not excluded by the objective manipulation test, there remains a significant relationship between reaction time and performance on the objective test (beta=0.0001, SE=0.00001, t(2529)=2.035, p < 0.05). These data suggest that subjects who perform highly on the objective test tend to have higher reaction times. Since only subjects who performed less than significantly above chance (< .6) on the objective tetst were kept, this suggests that the sample is biased towards subjects who also have faster reaction times.

Your own analysis
-----------------

Show us what you would do with these data, operating from first principles. What's the fairest plot showing a test of Sklar et al.'s original hypothesis that people can do arithmetic "non-consciously"?

I believe a fair plot to test this hypothesis is a logistic regression testing for the relationship between reaction time and the priming condition. There appears to be no relationship between the two by looking at the graph.


```r
ggplot(d.all.tidy, aes(x=RT, y=congruent)) + geom_point() +
  stat_smooth(method="glm", family="binomial", se=FALSE)
```

```
## Warning: glm.fit: algorithm did not converge
```

![plot of chunk unnamed-chunk-26](figure/unnamed-chunk-26-1.png) 

Challenge problem: Do you find any statistical support for Sklar et al.'s findings?

I here construct the actual linear model to determine the degree of relationship between reaction time and the priming condition. If Sklar's findings are accurate, then there should be a relationship between the two. However, instead we see there is no significant relationship between reactino time and the priming condition (beta=-0.0002, SE=0.0002, z=-1.05, p=0.294). There is still a relationship between the type of arithmetic problem being solved (addition or subtraction) and the subject's reaction time.


```r
assessment2 <- glm(operand ~ RT, family=binomial, d.all.tidy, na.action = na.omit)
print(summary(assessment2))
```

```
## 
## Call:
## glm(formula = operand ~ RT, family = binomial, data = d.all.tidy, 
##     na.action = na.omit)
## 
## Deviance Residuals: 
##    Min      1Q  Median      3Q     Max  
## -1.389  -1.145  -1.029   1.195   1.679  
## 
## Coefficients:
##               Estimate Std. Error z value Pr(>|z|)    
## (Intercept)  0.5926687  0.1285359   4.611 4.01e-06 ***
## RT          -0.0010083  0.0001891  -5.332 9.70e-08 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## (Dispersion parameter for binomial family taken to be 1)
## 
##     Null deviance: 8628  on 6230  degrees of freedom
## Residual deviance: 8599  on 6229  degrees of freedom
## AIC: 8603
## 
## Number of Fisher Scoring iterations: 4
```

```r
assessment <- glm(congruent ~ RT, family=binomial, d.all.tidy, na.action = na.omit)
print(summary(assessment))
```

```
## 
## Call:
## glm(formula = congruent ~ RT, family = binomial, data = d.all.tidy, 
##     na.action = na.omit)
## 
## Deviance Residuals: 
##    Min      1Q  Median      3Q     Max  
## -1.222  -1.176  -1.131   1.179   1.266  
## 
## Coefficients:
##               Estimate Std. Error z value Pr(>|z|)
## (Intercept)  0.1254691  0.1260606   0.995    0.320
## RT          -0.0001942  0.0001849  -1.050    0.294
## 
## (Dispersion parameter for binomial family taken to be 1)
## 
##     Null deviance: 8638.0  on 6230  degrees of freedom
## Residual deviance: 8636.9  on 6229  degrees of freedom
## AIC: 8640.9
## 
## Number of Fisher Scoring iterations: 3
```
