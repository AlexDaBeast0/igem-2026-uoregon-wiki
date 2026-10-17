---
layout: page
permalink: /description

title: Description
subtitle: A high-level overview of the entire project.
banner: https://static.igem.wiki/teams/6041/wiki/page-banners/banner-metolius-pink-flower.avif
---

{% include box.html 
    text="Nitrogen-based fertilizers are an essential component of modern agriculture across the globe. Despite this, only around half of this nitrogen is absorbed by plants; the rest may leach into the soil as nitrate, eventually reaching groundwater, wells, and surface waters. This excess nitrate can cause major harm to ecosystems, causing eutrophication and making it difficult for aquatic life to survive. Additionally, drinking nitrate-contaminated water can lead to adverse health effects. To combat this issue, bacteria is engineered to sequester and store excess environmental nitrate within the cell for recycling into agricultural pipelines. Through this approach, we hope to achieve more sustainable practices for nitrogen use, access to clean drinking water for rural households, and bioremediation in wastewater systems."
%}

# Our solution

Nitrate is naturally used as a nitrogen source for many bacteria, however, those already found within these agricultural systems cannot keep up with the extreme volume of the fertilizers used. Because of this, we decided to engineer *Escherichia coli* to uptake nitrate at a high rate and convert it into more biologically useful forms of nitrogen, before being collected for reuse as a fertilizer. These engineered bacteria would be implemented within filtration systems in locations such as (but not limited to) private wells and wastewater systems, allowing the excess nitrates to be collected before they can effect people and the environment.

This strategy was chosen to allow for not only the removal of harmful nitrates, but also to make nitrogen fertilizer reusable for rural farming communities. Nitrogen fertilizer is necessary but quite expensive. By implementing the engineered bacteria within a filtration system, it allows for easy containment of our bacteria, along with a point of access for collection of the nitrogen-enriched bacteria.

# Project design

In order to achieve this solution, our project has three major components: [chassis optimization](/uoregon/chassis), [storage](/uoregon/nitrogen-storage), and [flocculation](/uoregon/flocculation). For uptake we focused on testing the existing uptake limits the BL21* (DE3) strain of *Escherichia coli*, and used the results to guide our engineering approach. Specifically, we looked at altering the existing NarK/NarU nitrate import system naturally in *E. coli*. For storage, we wanted to ensure the converted nitrogen would remain in a metabolically useful form, without being sequestered into possible pathways. To do this, we decided to store our nitrogen in the form of cyanophycin, a biopolymer consisting of an aspartate backbone with arginine residues. For collection, we needed a method to separate cells containing cyanophycin from those that had not yet sufficiently sequestered nitrogen. This was accomplished by overexpression of the bacterial *bcsb* gene in cells with sequestered nitrogen. Expression of this gene is associated with enhanced formation of cellular flocculates, allowing for inducible and selective filtration of aggregated biomass. 

# Computational project

To ensure high nitrogen content in the bacteria recycled from our system, flocculation had to occur only once they sequestered a high amount of nitrogen. We worked to design a biosensor sensitive to the amount of cyanophycin storage polymer in the engineered bacteria. There was no existing biosensor for cyanophycin, making this a promising target for computational protein design. We designed *de novo* binders using motif scaffolding in RFDiffusion and ProteinMPNN. The details of this module are outlined in the [corresponding page](/uoregon/split-biosensor).

# Outreach

Our outreach has included our campus-wide and academic communities, as well as human practices experts from around the Willamette Valley. To better understand the needs and constraints surrounding nitrate remediation and fertilizer use, we have engaged with experts in wastewater treatment, farming, and education. 

Our [educational work](/uoregon/education) has included a series of workshops aimed at high-school and undergraduate students. These workshops cover synthetic biology fundamentals, bioethics, and science communication, along with hands-on activities designed around each topic.
