# Requirements Viewpoints

Dieses Dokument fasst die in der MDG-Datei definierten Requirement Viewpoints des NAFv4-ADMBw-Profils zusammen und verweist auf die strukturierte JSON-Datei `requirement_viewpoints.json`.

## Diagrammtypen

| Kennung | Name | Diagrammtyp | Toolbox | Beschreibung |
| --- | --- | --- | --- | --- |
| R2 | R2 - Requirement Catalogue | Diagram_Custom | NAFv4-ADMBw-R2-Toolbox | The R2 represents a catalog of requirements in the architectural model. For this purpose, categories can be created in which the functional and non-functional requirements can be grouped. |
| R3 | R3 - Requirement Dependencies | Diagram_Custom | NAFv4-ADMBw-R3-Toolbox | The R3 is used to show dependencies between different requirements. |
| R7 | R7 - Requirement Derivation | Diagram_Custom | NAFv4-ADMBw-R7-Toolbox | The R7 assigns functional and non-functional requirements to the demanding architectural elements. In addition, information about the planned realization can be shown. |
| R8 | R8 - Requirement Fulfilment | Diagram_Custom | NAFv4-ADMBw-R8-Toolbox | The R8 is used to determine and map acceptance and evaluation criteria for the individual functional and non-functional requirements. |
| Rr | Rr - Requirement Realization | Diagram_Custom | NAFv4-ADMBw-Rr-Toolbox | In the Rr, requirements are assigned to the realizing architectural elements. |

### R2 – R2 - Requirement Catalogue

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-R2-Toolbox`
- Zweck: The R2 represents a catalog of requirements in the architectural model. For this purpose, categories can be created in which the functional and non-functional requirements can be grouped.

**R2-Elements && Relationships**

_Elemente:_
- **FunctionalRequirement** (`Requirement`) – The element represents a functional requirement (what should the system / software be able to do?).
- **NonfunctionalRequirement** (`Requirement`) – The element represents a non-functional requirement (how should the system / software be able to do something?).
- **RequirementCatalogue** (`Class`) – Element represents a catalog of requirements, which consists of different categories (RequirementCategory) of functional and non-functional requirements.
- **RequirementCategory** (`Class`) – Element represents a category of a catalog of requirements.

_Beziehungen:_
- **PartOfCatalogue** (`Aggregation`) – This relation states that a category (RequirementCategory) belongs to a requirements catalog (RequirementCatalogue).
- **PartOfCategory** (`Aggregation`) – This relation states that his functional or non-functional requirement belongs to a category (RequirementCategory) of the requirements catalog.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Findings && Recommendations**

_Elemente:_
- **Finding** (`Class`) – An ascertainment made in the model, which relates to the methodology used, the subject under consideration, the tool or something else.
- **Recommendation** (`Class`) – Need for action from a finding.

_Beziehungen:_
- **RealizesRecommendation** (`Realization`) – Relation states that a Recommendation is realized through this element.
- **RefersTo** (`Dependency`) – Relationship that assigns a finding to a recommendation.
- **ResultsFrom** (`Dependency`) – Relationship expresses that an element of architecture is the reason for a finding.

**Stakeholder Concerns**

_Elemente:_
- **ActualOrganization** (`Object`) – An actual formal or informal organizational unit, e.g. "Driving and Vehicle Licensing Agency", "UAF team Alpha".
- **ActualPerson** (`Object`) – An individual human being.
- **ActualPost** (`Object`) – An actual, specific post, an instance of a Post "type" - e.g., "President of the United States of America." where the Post would be president.
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **Concern** (`Class`) – Interest in an EnterprisePhase (EnterprisePhase is synonym for System in ISO 42010) relevant to one or more of its stakeholders.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.

_Beziehungen:_
- **StakeholderConcern** (`Dependency`) – A relationship that expresses which concern a stakeholder has.

### R3 – R3 - Requirement Dependencies

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-R3-Toolbox`
- Zweck: The R3 is used to show dependencies between different requirements.

**R3-Elements && Relationships**

_Elemente:_
- **FunctionalRequirement** (`Requirement`) – The element represents a functional requirement (what should the system / software be able to do?).
- **NonfunctionalRequirement** (`Requirement`) – The element represents a non-functional requirement (how should the system / software be able to do something?).

_Beziehungen:_
- **ConflictsWith** (`Dependency`) – Relation that represents a conflict between two requirements.
- **IsDuplicateOf** (`Dependency`) – Relation that represents that two requirements convey the same content.
- **Refines** (`Dependency`) – Relation that represents a refinement of a requirement by another requirement.
- **Replaces** (`Dependency`) – Relation that represents a replacement of a requirement with another requirement.
- **Requires** (`Dependency`) – Relation that represents that a requirement assumes another requirement.
- **StemsFrom** (`Dependency`) – Relationship that states that one requirement stems from another.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Findings && Recommendations**

_Elemente:_
- **Finding** (`Class`) – An ascertainment made in the model, which relates to the methodology used, the subject under consideration, the tool or something else.
- **Recommendation** (`Class`) – Need for action from a finding.

_Beziehungen:_
- **RealizesRecommendation** (`Realization`) – Relation states that a Recommendation is realized through this element.
- **RefersTo** (`Dependency`) – Relationship that assigns a finding to a recommendation.
- **ResultsFrom** (`Dependency`) – Relationship expresses that an element of architecture is the reason for a finding.

**Stakeholder Concerns**

_Elemente:_
- **ActualOrganization** (`Object`) – An actual formal or informal organizational unit, e.g. "Driving and Vehicle Licensing Agency", "UAF team Alpha".
- **ActualPerson** (`Object`) – An individual human being.
- **ActualPost** (`Object`) – An actual, specific post, an instance of a Post "type" - e.g., "President of the United States of America." where the Post would be president.
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **Concern** (`Class`) – Interest in an EnterprisePhase (EnterprisePhase is synonym for System in ISO 42010) relevant to one or more of its stakeholders.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.

_Beziehungen:_
- **StakeholderConcern** (`Dependency`) – A relationship that expresses which concern a stakeholder has.

### R7 – R7 - Requirement Derivation

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-R7-Toolbox`
- Zweck: The R7 assigns functional and non-functional requirements to the demanding architectural elements. In addition, information about the planned realization can be shown.

**R7-Elements && Relationships**

_Elemente:_
- **FunctionalRequirement** (`Requirement`) – The element represents a functional requirement (what should the system / software be able to do?).
- **NonfunctionalRequirement** (`Requirement`) – The element represents a non-functional requirement (how should the system / software be able to do something?).

_Beziehungen:_
- **DerivedFrom** (`Dependency`) – Relation that shows that a functional or non-functional requirement is based on a process, role and task carrier, information element or other element.
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.
- **Refines** (`Dependency`) – Relation that represents a refinement of a requirement by another requirement.
- **Requires** (`Dependency`) – Relation that represents that a requirement assumes another requirement.
- **ToBeRealizedBy** (`Dependency`) – Relation states that a functional or non-functional requirement should be realized through this element.

**Constraints && References**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **ResourceConstraint** (`Class`) – A rule governing the structural or functional aspects of an implementation.
- **ServicePolicy** (`Class`) – A constraint governing the use of one or more ServiceSpecifications.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Findings && Recommendations**

_Elemente:_
- **Finding** (`Class`) – An ascertainment made in the model, which relates to the methodology used, the subject under consideration, the tool or something else.
- **Recommendation** (`Class`) – Need for action from a finding.

_Beziehungen:_
- **RealizesRecommendation** (`Realization`) – Relation states that a Recommendation is realized through this element.
- **RefersTo** (`Dependency`) – Relationship that assigns a finding to a recommendation.
- **ResultsFrom** (`Dependency`) – Relationship expresses that an element of architecture is the reason for a finding.

**Stakeholder Concerns**

_Elemente:_
- **ActualOrganization** (`Object`) – An actual formal or informal organizational unit, e.g. "Driving and Vehicle Licensing Agency", "UAF team Alpha".
- **ActualPerson** (`Object`) – An individual human being.
- **ActualPost** (`Object`) – An actual, specific post, an instance of a Post "type" - e.g., "President of the United States of America." where the Post would be president.
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **Concern** (`Class`) – Interest in an EnterprisePhase (EnterprisePhase is synonym for System in ISO 42010) relevant to one or more of its stakeholders.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.

_Beziehungen:_
- **StakeholderConcern** (`Dependency`) – A relationship that expresses which concern a stakeholder has.

### R8 – R8 - Requirement Fulfilment

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-R8-Toolbox`
- Zweck: The R8 is used to determine and map acceptance and evaluation criteria for the individual functional and non-functional requirements.

**R8-Elements && Relationships**

_Elemente:_
- **FitCriterion** (`Class`) – This element represents an acceptance criterion for a functional or non-functional requirement.
- **FulfilmentCriterion** (`Class`) – This element represents a criterion for evaluating the degree of implementation of a functional or non-functional requirement.

_Beziehungen:_
- **Checks** (`Dependency`) – Relation that shows that an acceptance criterion (FitCriterion) is valid for a functional or non-functional requirement.
- **Evaluates** (`Realization`) – This relation states that an evaluation criterion (FulfilmentCriterion) can be assigned to a specific acceptance criterion (FitCriterion).

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Findings && Recommendations**

_Elemente:_
- **Finding** (`Class`) – An ascertainment made in the model, which relates to the methodology used, the subject under consideration, the tool or something else.
- **Recommendation** (`Class`) – Need for action from a finding.

_Beziehungen:_
- **RealizesRecommendation** (`Realization`) – Relation states that a Recommendation is realized through this element.
- **RefersTo** (`Dependency`) – Relationship that assigns a finding to a recommendation.
- **ResultsFrom** (`Dependency`) – Relationship expresses that an element of architecture is the reason for a finding.

**Stakeholder Concerns**

_Elemente:_
- **ActualOrganization** (`Object`) – An actual formal or informal organizational unit, e.g. "Driving and Vehicle Licensing Agency", "UAF team Alpha".
- **ActualPerson** (`Object`) – An individual human being.
- **ActualPost** (`Object`) – An actual, specific post, an instance of a Post "type" - e.g., "President of the United States of America." where the Post would be president.
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **Concern** (`Class`) – Interest in an EnterprisePhase (EnterprisePhase is synonym for System in ISO 42010) relevant to one or more of its stakeholders.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.

_Beziehungen:_
- **StakeholderConcern** (`Dependency`) – A relationship that expresses which concern a stakeholder has.

### Rr – Rr - Requirement Realization

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-Rr-Toolbox`
- Zweck: In the Rr, requirements are assigned to the realizing architectural elements.

**Rr-Realise**

_Beziehungen:_
- **RealiseRequirement** (`Realization`) – Relation states that a functional or non-functional requirement is realized through this element.

**Rr-Realizing Service**

_Elemente:_
- **ServiceFunction** (`Activity`) – An Activity that describes the abstract behavior of ServiceSpecifications, regardless of the actual implementation.
- **ServiceInterface** (`Class`) – A contract that defines the ServiceMethods and ServiceMessageHandlers that the ServiceSpecification realizes.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.
- **ServiceSpecificationRole** (`Part`) – An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality.

**Rr-Realizing Resources**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **Function** (`Activity`) – An Activity which is specified in the context to the ResourcePerformer (human or machine) that IsCapableToPerform it.
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **ResourceInterface** (`Class`) – A declaration that specifies a contract between the ResourcePerformers it is related to and any other ResourcePerformers it can interact with. It is also intended to be an implementation of a specification of an Interface in the Business and/or Service layer.
- **Software** (`Class`) – A sub-type of ResourceArtifact that specifies an executable computer program.
- **System** (`Class`) – An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements (INCOSE SE Handbook V4, 2015).

**Rr-Realizing Organizations**

_Elemente:_
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).

**Rr-Realizing Standards**

_Elemente:_
- **Protocol** (`Class`) – A Standard for communication over a network. Protocols may be composite, represented as a ProtocolStack made up of ProtocolLayers.
- **Protocolstack** (`Class`) – A sub type of Protocol that contains the ProtocolLayers, defining a complete stack.
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

**Rr-Realizing Measurement**

_Elemente:_
- **Measurement** (`Part`) – A property of an element representing something in the physical world, expressed in amounts of a unit of measure.
- **MeasurementType** (`Class`) – A type of a property representing something in the physical world, expressed in amounts of a unit of measure.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Findings && Recommendations**

_Elemente:_
- **Finding** (`Class`) – An ascertainment made in the model, which relates to the methodology used, the subject under consideration, the tool or something else.
- **Recommendation** (`Class`) – Need for action from a finding.

_Beziehungen:_
- **RealizesRecommendation** (`Realization`) – Relation states that a Recommendation is realized through this element.
- **RefersTo** (`Dependency`) – Relationship that assigns a finding to a recommendation.
- **ResultsFrom** (`Dependency`) – Relationship expresses that an element of architecture is the reason for a finding.

**Stakeholder Concerns**

_Elemente:_
- **ActualOrganization** (`Object`) – An actual formal or informal organizational unit, e.g. "Driving and Vehicle Licensing Agency", "UAF team Alpha".
- **ActualPerson** (`Object`) – An individual human being.
- **ActualPost** (`Object`) – An actual, specific post, an instance of a Post "type" - e.g., "President of the United States of America." where the Post would be president.
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **Concern** (`Class`) – Interest in an EnterprisePhase (EnterprisePhase is synonym for System in ISO 42010) relevant to one or more of its stakeholders.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.

_Beziehungen:_
- **StakeholderConcern** (`Dependency`) – A relationship that expresses which concern a stakeholder has.