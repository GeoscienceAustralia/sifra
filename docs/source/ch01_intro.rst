.. _intro-page:

************
Introduction
************

Critical infrastructure facilities typically comprise a number of 
interconnected components that work in concert to deliver a service. 
In the context of natural hazard vulnerability, the components have differing 
susceptibilities, require different resource levels and time to repair, and 
have a range of criticalities to the overall service delivery. The 
vulnerability of the facility, then, is a product of the components,
their properties and interactions.

SIRA stands for *Systemic Infrastructure Resilience Analysis*.
It comprises a method and software tools that provide a framework for 
simulating the fragility of infrastructure facilities to natural hazards, 
based on assessment of the fragilities and configuration of components that 
comprises the facility. Currently the system is designed to work with 
earthquake hazards only. ``SIRA`` enables the vulnerabilities of each element
to be within a facility or a network to be integrated into a holistic
assessment of the direct system losses, service disruption and cost.

SIRA is used to model the vulnerability of high-value infrastructure
facilities to natural hazards. Earthquake ground motion is the present focus 
and many uncertainties are captured through a Monte Carlo sampling process. 
The tool facilitates quantification of infrastructure assets' vulnerability,
and also enables the most vulnerable components to be identified in terms of
repair cost, time to recovery, and service disruption implications. The 
outcomes also support benefit-versus-cost studies of retrofit options.
SIRA helps generate information that supports asset managers in regards
to the most cost-effective utilisation of limited retrofit resources.


.. _intro-design-notes:

:term:`Vulnerability <vulnerability>` of a facility is modelled by assigning 
fragilities to the individual components that make up a facility or a network.
The program accounts for variability in component fragilities by sampling
probability distributions for the each fragility curve median and beta values.
Once values have been selected for each curve it checks that
:term:`fragility curves` do not overlap and if they do, re-samples the
median and beta probability distributions until non-overlapping fragility
curves are produced.

Damage scales for most facility types, along with the recovery time estimation
method, has been taken from HAZUS :cite:`FEMA2003`. Although, where deemed more
appropriate, custom damage scales have been used, e.g. for electrical
substations.
Repair cost (and hence damage index) and recovery times for each component are
customised for each asset type, based on consultation with assets operators.
The threshold values of spectral acceleration for each of four damage states 
are sampled by randomly sampling the fragility curves described above.

Hazard modelling is done externally using other applications, and provided to
this tool as an input.
