# PyCascades
PyCascdes 2025 Demo

[Brainstorming](https://ohsucomputationalbio.slack.com/canvas/C07TZ82UVC5)
1. Potential Ideas / Components

* customizing a submission process in Python for the gen3 platform
* Data Structures for Scalable and Efficient Machine Learning (also questions that can be asked/answered). focusing on BMEG
* Combination of the above? Our current title is “Data Science Garage: Building Tools for Genomic Research”
* Can we add the new machine learning feature extraction paper in ^ . (was it done by randomForest  :melting_face:)
* Predicting molecular subtypes: data tutorial with scikit learn. Related ideas...
    * future BK paper on molecular subtyping
    * breast cancer grabbing mafs and finding most mutated genes

1. Potential Talk flow and time breakdown example


GDC BioBlend
PyGrip
Xena
cBioPortal
Prevalent mutations in cancer subtypes (e.g. most common mutation in breast cancer, hotspots across proteins)
Include AI!
Grid search of scikit-learn pipelines
End-to-end, multistep walkthrough of:

* Finding data
* Analyze data,
* Visualize data


Action Items

* Chat with Nasim about FHIR Aggregator or CDA as Python demo
* Which resources we’ll pull from?
* Which transformations?
* Which figures?
* E.g. Mutex for Cancer mutations or Machine Learning
* scikit-learn pipeline — TMP Paper (tarball with all cancers and subtypes), pandas operations to subset information and create ML model that recognizes that
    * Basal vs Luminal
    * Mutual Exclusivity Matrix (e.g. like BK has presented)
* Meet January 9th in afternoon before Nasim heads out
* Create hidden repo in ohsu-comp-bio

#### Workflow 
1. Introduction of the team (get headshots)
2. Background - define the problem + define complexity of the problem + how the elements of our stack tackles the problem 
   - Scientific problem = How can we find (actionable) insights in a disease as complex as cancer? 
   - Complexity = Has 1 ... * subtypes that at the molecular level behaves differently  
   - Clinical research endpoints + evidence = clinical utility (disease management + therapeutic decision making)
   - how the elements of our stack (has been attempting - work in progress) to tackles the problem
3. (essential intro to main topic) Data + python (ETL, glued by Liam’s devops) = structure / standard / size / enables xyz. FHIR Aggregator and CDA can come in (also VRS can be mentioned)
4. (Main topic) Machine Learning + python (algorithms) 
   - Matrix (excel) to FHIR Observation entity - quick (BMEG - grip) 
   - scikit-learn pipeline — TMP Paper (tarball with all cancers and subtypes)
      pandas operations to subset information and create ML model that recognizes that
      Basal vs Luminal (in spreadsheet) this is the category you are looking for from paper. Specialists in different organizations have categorized these - ex. molecular biologists.
   - Mutual Exclusivity Matrix (e.g. like BK has presented)
5. Conclusion = Connect the dots 
