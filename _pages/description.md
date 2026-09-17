---
layout: page
permalink: /description

title: Description
subtitle: A high-level overview of the entire project.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---

{% include box.html 
    heading="Abstract"
    heading-size="large"
    text="Nitrogen based fertilizers are an essential component of modern agriculture across the globe. Despite this, only around half of the nitrogen can be taken up by the plants; the rest seeps into the soil and groundwater in the form of nitrate, eventually reaching bodies of water, in addition to wells and sub-surface drainage systems. This excess nitrate can cause major harm to the existing ecosystems, making it difficult for aquatic life to survive. Additionally, drinking nitrate-contaminated water can lead to dangerous health ramifications such as respiratory distress, abdominal cramping, vomiting, thyroid dysfunction, or bladder cancers. To combat this issue, we engineered *Escherichia coli* to uptake excess nitrate and convert it into more biologically useful forms of nitrogen that can later be reused as fertilizers. This approach was chosen as a means to address sustainability in agriculture, access to clean drinking water for rural farmers, and bioremediation in wastewater systems all at the same time."
%}

# Background

The team was originally interested in three main projects: combating biofilms on medical catheters, a more sustainable way for farmers to get rid of their high-cellulose excess crops, and a way to remove pharmaceuticals from wastewater systems. After spending a few weeks researching these and coming up with potential projects, the team became more interested in sustainability for farmers and cleaning up wastewater systems. We had a difficult time deciding between the two, so we chose to combine aspects of each potential project, eventually landing on making agriculture more sustainable while simultaneously cleaning up wastewater systems (and more) by targeting nitrogen-fertilizers, reducing their waste and harmful runoff.

Nitrogen based fertilizers are an essential component of modern agriculture across the globe. Despite this, only around half of the nitrogen can be taken up by the plants; the rest seeps into the soil and groundwater in the form of nitrate, eventually reaching bodies of water, in addition to wells and sub-surface drainage systems. This excess nitrate can cause major harm to the existing ecosystems, making it difficult for aquatic life to survive. Additionally, drinking nitrate-contaminated water can lead to dangerous health ramifications such as respiratory distress, abdominal cramping, vomiting, thyroid dysfunction, or bladder cancers.

# Our solution

Nitrate is naturally used as a nitrogen source for many bacteria, however, those already found within these agricultural systems cannot keep up with the extreme volume of the fertilizers used. Because of this, we decided to engineer *Escherichia coli* to uptake nitrate at a high rate and convert it into more biologically useful forms of nitrogen, before being collected for reuse as a fertilizer. These engineered bacteria would be implemented within filtration systems in locations such as (but not limited to) private wells and wastewater systems, allowing the excess nitrates to be collected before they can do harm to people and the environment.

This strategy was chosen to allow for not only the removal of harmful nitrates, but also to make nitrogen fertilizer reusable for rural farming communities, as it's necessary but quite expensive. By implementing within a filtration system, it allows for the easy containment of our bacteria (so as not to contaminate drinking water or disrupt existing bacterial communities), along with a point of access for collection of the nitrogen rich bacteria.

# How we built the solution (a bit of technical detail).

In order to achieve this solution, our project has three major components: uptake, storage, and collection. For uptake, we focused on testing the existing uptake limits, and working off of the results to influence our engineering approach. Specifically, we looked at altering the existing NarK/NarU import system naturally in *Escherichia coli*. For storage, we wanted to ensure the converted nitrogen would remain in a useful form, without being sequestered throughout the many possible metabolic pathways. To do this, we decided to store our nitrogen in the form of cyanophycin, a biopolymer consisting of an aspartate backbone with arginine residues. For collection, we needed a way to distinguish between the nitrogen rich bacteria and the bacteria that still had a capacity to uptake more. We chose to use flocculation to accomplish this, leveraging an addition of the *bcsb* gene with inducible expression. This gives us the ability to induce flocculation within our system, making it much easier to collect the bacteria, since it will sink once flocculated.

# Summary of comp projects.

To ensure high nitrogen content in the bacteria, we realized that flocculation had to occur only once they sequestered a high amount of nitrogen. Sensing the amount of cyanophycin storage polymer in the bacteria would be a good approach here. However, we could not find an existing biosensor for cyanophycin. We identified this problem as a promising target for computational protein design. We designed *de novo* binders using motif scaffolding in RFDiffusion and ProteinMPNN. The details of this module are outlined in the [corresponding page](/uoregon/split-biosensor).

# Summary of our outreach/outreach activities.
