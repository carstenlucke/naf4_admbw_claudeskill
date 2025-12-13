# Logical Specification Viewpoints

Zusammenfassung der Logical Specification Viewpoints inklusive Diagrammtypen, zugehörigen Toolboxes und erlaubten Elemente/Beziehungen. Detaildaten siehe `logical_specification_viewpoints.json`.

| Kennung | Name | Diagrammtyp | Toolbox | Beschreibung |
| --- | --- | --- | --- | --- |
| Business Process | Business Process | Diagram_Analysis | NAFv4-ADMBw-BusinessProcess-Toolbox |  |
| L1 | L1 - Node Types | Diagram_Custom | NAFv4-ADMBw-L1-Toolbox | The L1 Viewpoint defines all of the Nodes that will appear in a Logical Architecture. Nodes are elements of capability assembled and orchestrated in the Logical Architecture (see L2 - Logical Scenario and L4 - Logical Activities views). The levels of capability provided by each node are expressed as Measures of Performance (MoPs) and these may be dependent on the environments in which the Node is required to operate. |
| L2 | L2 - Logical Scenario | Diagram_Custom | NAFv4-ADMBw-L2-Toolbox | The L2 Viewpoint specifies Nodes (elements of capability) in context of each other. The context is usually expressed in terms of the information that flows between the nodes (e.g. the information flow requirements between capabilities in a given scenario) but may also be flows of materiel, human resource or energy. |
| L3 | L3 - Node Interactions | Diagram_Custom | NAFv4-ADMBw-L3-Toolbox | L3 is used to provide further detail of the interoperability requirements associated with the operational capability of interest. The focus is on logical flows that cross the capability boundary. Although the primary purpose of the L3 Viewpoint is to specify information exchanges, the L3 may also list flows of materiel, energy and human resources. |
| L4 | L4 - Logical Activities | Diagram_Custom | NAFv4-ADMBw-L4-Toolbox | The L4 Viewpoint describes the operational activities that are being conducted within the mission or scenario. These activities are defined at a logical, solution-neutral level so as to enable different solutions in the physical layer. The L4 Viewpoint describes the activities associated with the logical architecture, as well as the: |
| L5 | L5 - Logical States | Diagram_Custom | NAFv4-ADMBw-L5-Toolbox | The L5 Viewpoint specifies the typical states a node may have and the possible transitions between those states (i.e. changes of state). Triggers for state changes may also be defined. Actions may be associated with a given state or with the transition between states in response to stimuli (e.g. triggers and events). |
| L6 | L6 - Logical Sequence | Diagram_Sequence | NAFv4-ADMBw-L6-Toolbox | Operational Event-Trace Descriptions, sometimes called sequence diagrams, event scenarios or timing diagrams, allow the tracing of interactions between nodes in a scenario or critical sequence of events. The node interactions usually correspond to flows of information but may describe flows of energy, materiel or people specified in the L2, Logical Scenario. |
| L7 | L7 - Information Model | Diagram_Custom | NAFv4-ADMBw-L7-Toolbox | The L7 Viewpoint is used to document the business information. It describes the information that can be exchanged along the logical flows in the architecture, specified in L3 Node Interactions. |
| L8 | L8 - Logical Constraints | Diagram_Custom | NAFv4-ADMBw-L8-Toolbox | The L8 Viewpoint is used to constrain the logical architecture without forcing a particular solution. L8 is used for rules which are not expressed as behavioural models, interactions or measures of effectiveness, i.e. they are textual statements of requirements that constrain the architecture. |
| Lr | Lr - Lines of Development | Diagram_Custom | NAFv4-ADMBw-Lr-Toolbox | The Lr Viewpoint is primarily intended to support the acquisition process across multiple projects or programmes, highlighting dependencies the logical dependencies between capabilities, projects and the integration of all lines of development to achieve a successfully integrated military capability. Use of the Lr Viewpoint should support the management of capability delivery and be aligned with Cr, Capability Roadmap. |
| L2-L3 | L2-L3 - Logical Concept | Diagram_Custom | NAFv4-ADMBw-L2-L3-Toolbox | The L2-L3 Viewpoint is concerned with providing an executive level, scenario-based communication of the architecture purpose, scope and content. |

## Business Process – Business Process

- Diagrammtyp: `Diagram_Analysis`
- Toolbox: `NAFv4-ADMBw-BusinessProcess-Toolbox`
- Zweck: Kein Beschreibungstext vorhanden.

**NAFv4-ADMBw-BusinessProcess-Toolbox::hidden**

_Elemente:_
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.
- **OperationalRole** (`Part`) – Usage of a OperationalPerformer or OperationalArchitecture in the context of another OperationalPerformer or OperationalArchitecture. Creates a whole-part relationship.

**Process modeling**

_Elemente:_
- **EndEvent** (`Event`) – Keine Beschreibung definiert.
- **Gateway** (`Decision`) – Keine Beschreibung definiert.
- **IntermediateEvent** (`Event`) – Keine Beschreibung definiert.
- **Lane** (`ActivityPartition`) – Keine Beschreibung definiert.
- **Pool** (`ActivityPartition`) – Keine Beschreibung definiert.
- **StartEvent** (`Event`) – Keine Beschreibung definiert.
- **TextAnnotation** (`Note`) – Keine Beschreibung definiert.
- **OperationalActivity** (`Activity`) – An Activity that captures a logical process, specified independently of how the process is carried out.
- **OperationalActivityAction** (`Action`) – A call of an OperationalActivity in the context of another OperationalActivity.

_Beziehungen:_
- **OperationalControlFlow** (`ControlFlow`) – An ActivityEdge that shows the flow of control between OperationalActivityActions.
- **OperationalMessageFlow** (`ControlFlow`) – A ProcessMessageFlow that shows the flow of message between OperationalActivityActions of different ActivityPartitions like Pools.
- **OperationalObjectFlow** (`ObjectFlow`) – An ActivityEdge that shows the flow of Resources (objects/information) between OperationalActivityActions.

**assign to Operational Agents / Service**

_Beziehungen:_
- **Consumes** (`Abstraction`) – A tuple that asserts that a service in someway contributes or assists in the execution of an OperationalActivity.
- **IsCapableToPerform** (`Abstraction`) – A relationship that says that a capable element performs an activity or action.
- **PerformsInContext** (`Abstraction`) – A relationship that says that a role performs an activity or action. It indicates that the action can be carried out by the role when used in a specific context or configuration.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

**ActsUpon**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **GeoPoliticalExtentType** (`DataType`) – A geospatial extent whose boundaries are defined by declaration or agreement by political parties.
- **InformationElement** (`Class`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable to perform (see IsCapableToPerform).
- **InformationRole** (`Part`) – A usage of InformationElement that exists in the context of an OperationalAsset. It also allows the representation of the whole-part aggregation of InformationElements.
- **KnownResource** (`Class`) – Asserts that a known ResourcePerformer constrains the implementation of the OperationalPerformer that plays the role in the LogicalArchitecture.
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **OperationalSignal** (`Signal`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable of performing (see IsCapableToPerform).
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **PaperForm** (`Class`) – Form is a digitized or digitizable document, for example a scanned document.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **Software** (`Class`) – A sub-type of ResourceArtifact that specifies an executable computer program.
- **System** (`Class`) – An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements (INCOSE SE Handbook V4, 2015).

_Beziehungen:_
- **ActsUpon** (`Dependency`) – Asserts that something (subject) is acted upon by an OperationalActivity (activity).

**Implement**

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.

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

## L1 – L1 - Node Types

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L1-Toolbox`
- Zweck: The L1 Viewpoint defines all of the Nodes that will appear in a Logical Architecture. Nodes are elements of capability assembled and orchestrated in the Logical Architecture (see L2 - Logical Scenario and L4 - Logical Activities views). The levels of capability provided by each node are expressed as Measures of Performance (MoPs) and these may be dependent on the environments in which the Node is required to operate.

**L1-Elements**

_Elemente:_
- **OperationalActivity** (`Activity`) – An Activity that captures a logical process, specified independently of how the process is carried out.
- **OperationalActivityAction** (`Action`) – A call of an OperationalActivity in the context of another OperationalActivity.
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.
- **OperationalRole** (`Part`) – Usage of a OperationalPerformer or OperationalArchitecture in the context of another OperationalPerformer or OperationalArchitecture. Creates a whole-part relationship.

**L1-Relationships**

_Elemente:_
- **Environment** (`Class`) – A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using EnvironmentKind.

_Beziehungen:_
- **EnvironmentalCondition** (`Dependency`) – Relationship that indicates under which environment an exhibits-relationship takes place.
- **Exhibits** (`Abstraction`) – A tuple that exists between a CapableElement and a Capability that it meets under specific environmental conditions.
- **MapsToCapability** (`Abstraction`) – A tuple denoting that an Activity contributes to providing a Capability.
- **PropertySetGeneralisation** (`Generalization`) – A PropertySetGeneralization is a taxonomic relationship between a more general PropertySet and a more specific PropertySet.

**Measurements**

_Elemente:_
- **ActualCondition** (`Object`) – An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed.
- **ActualEnvironment** (`Object`) – The ActualState that describes the circumstances of an Environment.
- **ActualLocation** (`Object`) – The ActualState that describes a physical location, for example using text to provide an address, Geo-coordinates, etc.
- **Measurement** (`Part`) – A property of an element representing something in the physical world, expressed in amounts of a unit of measure.
- **MeasurementType** (`Class`) – A type of a property representing something in the physical world, expressed in amounts of a unit of measure.

_Beziehungen:_
- **EnvironmentalContext** (`Dependency`) – Relationship that indicates under which condition an measurement counts.
- **OwnsMeasurement** (`Dependency`) – A relationship that expresses which measurement or measurement type an element owns.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

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

## L2 – L2 - Logical Scenario

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L2-Toolbox`
- Zweck: The L2 Viewpoint specifies Nodes (elements of capability) in context of each other. The context is usually expressed in terms of the information that flows between the nodes (e.g. the information flow requirements between capabilities in a given scenario) but may also be flows of materiel, human resource or energy.

**L2-Elements**

_Elemente:_
- **KnownResource** (`Class`) – Asserts that a known ResourcePerformer constrains the implementation of the OperationalPerformer that plays the role in the LogicalArchitecture.
- **OperationalArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the Operational perspective.
- **OperationalInterface** (`Class`) – A declaration that specifies a contract between the OperationalPerformer it is related to, and any other OperationalPerformers it can interact with.
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.
- **OperationalPort** (`Port`) – An interaction point for an OperationalAgent through which it can interact with the outside environment and which is defined by an OperationalInterface.
- **OperationalRole** (`Part`) – Usage of a OperationalPerformer or OperationalArchitecture in the context of another OperationalPerformer or OperationalArchitecture. Creates a whole-part relationship.
- **ProblemDomain** (`Part`) – A property associated with a logical architecture, used to specify the scope of the problem.

**L2-Relationships**

_Beziehungen:_
- **OperationalConnector** (`Connector`) – A Connector that goes between OperationalRoles representing a need to exchange Resources. It can carry a number of OperationalExchanges.
- **OperationalExchange** (`InformationFlow`) – Asserts that a flow can exist between OperationalPerformers (i.e. flows of information, people, materiel, or energy).

**Condition, Environment && Location**

_Elemente:_
- **ActualCondition** (`Object`) – An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed.
- **ActualEnvironment** (`Object`) – The ActualState that describes the circumstances of an Environment.
- **ActualLocation** (`Object`) – The ActualState that describes a physical location, for example using text to provide an address, Geo-coordinates, etc.
- **Condition** (`Class`) – A type that defines the Location, Environment and/or GeoPoliticalExtent.
- **Environment** (`Class`) – A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using EnvironmentKind.
- **Location** (`Class`) – A specification of the generic area in which a LocationHolder is required to be located.

_Beziehungen:_
- **LocationType** (`Dependency`) – A relationship that expresses which location is assigned to a location holder.
- **PhysicalLocation** (`Dependency`) – A relationship that expresses that a location holder operates in an actual location.
- **RequiredEnvironment** (`Dependency`) – A relationship that expresses that a location holder operates under specific environmental conditions.

**Measurements**

_Elemente:_
- **Measurement** (`Part`) – A property of an element representing something in the physical world, expressed in amounts of a unit of measure.
- **MeasurementType** (`Class`) – A type of a property representing something in the physical world, expressed in amounts of a unit of measure.

_Beziehungen:_
- **EnvironmentalContext** (`Dependency`) – Relationship that indicates under which condition an measurement counts.
- **OwnsMeasurement** (`Dependency`) – A relationship that expresses which measurement or measurement type an element owns.

**L2-Operational Exchange Items**

_Elemente:_
- **Energy** (`Class`) – A representation of any kind of energy.
- **GeoPoliticalExtentType** (`DataType`) – A geospatial extent whose boundaries are defined by declaration or agreement by political parties.
- **InformationElement** (`Class`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable to perform (see IsCapableToPerform).
- **KnownResource** (`Class`) – Asserts that a known ResourcePerformer constrains the implementation of the OperationalPerformer that plays the role in the LogicalArchitecture.
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **OperationalSignal** (`Signal`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable of performing (see IsCapableToPerform).
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **Responsibility** (`Class`) – The type of duty required of a Person or Organization.

**L2-Operational Constraints**

_Elemente:_
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.

_Beziehungen:_
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
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

## L3 – L3 - Node Interactions

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L3-Toolbox`
- Zweck: L3 is used to provide further detail of the interoperability requirements associated with the operational capability of interest. The focus is on logical flows that cross the capability boundary. Although the primary purpose of the L3 Viewpoint is to specify information exchanges, the L3 may also list flows of materiel, energy and human resources.

**L3-Nodes**

_Elemente:_
- **KnownResource** (`Class`) – Asserts that a known ResourcePerformer constrains the implementation of the OperationalPerformer that plays the role in the LogicalArchitecture.
- **OperationalArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the Operational perspective.
- **OperationalInterface** (`Class`) – A declaration that specifies a contract between the OperationalPerformer it is related to, and any other OperationalPerformers it can interact with.
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.
- **OperationalRole** (`Part`) – Usage of a OperationalPerformer or OperationalArchitecture in the context of another OperationalPerformer or OperationalArchitecture. Creates a whole-part relationship.
- **ProblemDomain** (`Part`) – A property associated with a logical architecture, used to specify the scope of the problem.

**L3-Node Relationships**

_Elemente:_
- **OperationalPort** (`Port`) – An interaction point for an OperationalAgent through which it can interact with the outside environment and which is defined by an OperationalInterface.

_Beziehungen:_
- **OperationalConnector** (`Connector`) – A Connector that goes between OperationalRoles representing a need to exchange Resources. It can carry a number of OperationalExchanges.
- **OperationalExchange** (`InformationFlow`) – Asserts that a flow can exist between OperationalPerformers (i.e. flows of information, people, materiel, or energy).

**L3-Activities**

_Beziehungen:_
- **IsCapableToPerform** (`Abstraction`) – A relationship that says that a capable element performs an activity or action.
- **PerformsInContext** (`Abstraction`) – A relationship that says that a role performs an activity or action. It indicates that the action can be carried out by the role when used in a specific context or configuration.

**L3-OperationalExchangeItems**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **Energy** (`Class`) – A representation of any kind of energy.
- **GeoPoliticalExtentType** (`DataType`) – A geospatial extent whose boundaries are defined by declaration or agreement by political parties.
- **InformationElement** (`Class`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable to perform (see IsCapableToPerform).
- **InformationRole** (`Part`) – A usage of InformationElement that exists in the context of an OperationalAsset. It also allows the representation of the whole-part aggregation of InformationElements.
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **OperationalSignal** (`Signal`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable of performing (see IsCapableToPerform).
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **PostRole** (`Class`) – A usage of a post in the context of another OrganizationalResource. Creates a whole-part relationship.
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **Responsibility** (`Class`) – The type of duty required of a Person or Organization.
- **SubOrganization** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).

**L3-Services**

_Elemente:_
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.
- **ServiceSpecificationRole** (`Part`) – An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality.

_Beziehungen:_
- **ConsumedBy** (`Dependency`) – Asserts that a service is consumed by a node. It is not required to know what provides the service.
- **Provides** (`Dependency`) – Asserts that a operational agent provides a service.

**Condition, Environment && Location**

_Elemente:_
- **ActualCondition** (`Object`) – An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed.
- **ActualEnvironment** (`Object`) – The ActualState that describes the circumstances of an Environment.
- **ActualLocation** (`Object`) – The ActualState that describes a physical location, for example using text to provide an address, Geo-coordinates, etc.
- **Condition** (`Class`) – A type that defines the Location, Environment and/or GeoPoliticalExtent.
- **Environment** (`Class`) – A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using EnvironmentKind.
- **Location** (`Class`) – A specification of the generic area in which a LocationHolder is required to be located.

_Beziehungen:_
- **LocationType** (`Dependency`) – A relationship that expresses which location is assigned to a location holder.
- **PhysicalLocation** (`Dependency`) – A relationship that expresses that a location holder operates in an actual location.
- **RequiredEnvironment** (`Dependency`) – A relationship that expresses that a location holder operates under specific environmental conditions.

**Measurements**

_Elemente:_
- **ActualCondition** (`Object`) – An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed.
- **ActualEnvironment** (`Object`) – The ActualState that describes the circumstances of an Environment.
- **ActualLocation** (`Object`) – The ActualState that describes a physical location, for example using text to provide an address, Geo-coordinates, etc.
- **Measurement** (`Part`) – A property of an element representing something in the physical world, expressed in amounts of a unit of measure.
- **MeasurementType** (`Class`) – A type of a property representing something in the physical world, expressed in amounts of a unit of measure.

_Beziehungen:_
- **EnvironmentalContext** (`Dependency`) – Relationship that indicates under which condition an measurement counts.
- **OwnsMeasurement** (`Dependency`) – A relationship that expresses which measurement or measurement type an element owns.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
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

## L4 – L4 - Logical Activities

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L4-Toolbox`
- Zweck: The L4 Viewpoint describes the operational activities that are being conducted within the mission or scenario. These activities are defined at a logical, solution-neutral level so as to enable different solutions in the physical layer. The L4 Viewpoint describes the activities associated with the logical architecture, as well as the:

**L4-OperationalElements**

_Elemente:_
- **InformationElement** (`Class`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable to perform (see IsCapableToPerform).
- **InformationRole** (`Part`) – A usage of InformationElement that exists in the context of an OperationalAsset. It also allows the representation of the whole-part aggregation of InformationElements.
- **OperationalActivity** (`Activity`) – An Activity that captures a logical process, specified independently of how the process is carried out.
- **OperationalActivityAction** (`Action`) – A call of an OperationalActivity in the context of another OperationalActivity.
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.
- **OperationalRole** (`Part`) – Usage of a OperationalPerformer or OperationalArchitecture in the context of another OperationalPerformer or OperationalArchitecture. Creates a whole-part relationship.
- **StandardOperationalActivity** (`Activity`) – A sub-type of OperationalActivity that is a standard operating procedure.

**L4-Relationships**

_Beziehungen:_
- **AffectedActivity** (`Dependency`) – A relationship that expresses which resource is affected by a operational activity.
- **AffectedResource** (`Dependency`) – A relationship that expresses which operational activity is affected by a resource.
- **Consumes** (`Abstraction`) – A tuple that asserts that a service in someway contributes or assists in the execution of an OperationalActivity.
- **IsCapableToPerform** (`Abstraction`) – A relationship that says that a capable element performs an activity or action.
- **OperationalExchange** (`InformationFlow`) – Asserts that a flow can exist between OperationalPerformers (i.e. flows of information, people, materiel, or energy).
- **PerformsInContext** (`Abstraction`) – A relationship that says that a role performs an activity or action. It indicates that the action can be carried out by the role when used in a specific context or configuration.
- **ProcessGeneralization** (`Generalization`) – A ProcessGeneralization is a taxonomic relationship between a more general Process and a more specific Process.

**L4-ActsUpon**

_Elemente:_
- **GeoPoliticalExtentType** (`DataType`) – A geospatial extent whose boundaries are defined by declaration or agreement by political parties.
- **InformationElement** (`Class`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable to perform (see IsCapableToPerform).
- **KnownResource** (`Class`) – Asserts that a known ResourcePerformer constrains the implementation of the OperationalPerformer that plays the role in the LogicalArchitecture.
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **OperationalSignal** (`Signal`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable of performing (see IsCapableToPerform).
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **PaperForm** (`Class`) – Form is a digitized or digitizable document, for example a scanned document.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **Responsibility** (`Class`) – The type of duty required of a Person or Organization.

_Beziehungen:_
- **ActsUpon** (`Dependency`) – Asserts that something (subject) is acted upon by an OperationalActivity (activity).

**L4-Conditions**

_Elemente:_
- **ActualCondition** (`Object`) – An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed.

_Beziehungen:_
- **ActivityPerformableUnderCondition** (`Dependency`) – The ActualCondition under which an Activity is performed.

**L4-Service**

_Elemente:_
- **ActualService** (`Object`) – An individual ServiceSpecification.
- **RequiredServiceLevel** (`Object`) – A sub type of ActualService that details a specific service level required of the provider.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.

_Beziehungen:_
- **ActivitySupportsService** (`Realization`) – Relation states that a process is necessary for the implementation of a service.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

**References**

_Elemente:_
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).

**Implement**

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.

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

## L5 – L5 - Logical States

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L5-Toolbox`
- Zweck: The L5 Viewpoint specifies the typical states a node may have and the possible transitions between those states (i.e. changes of state). Triggers for state changes may also be defined. Actions may be associated with a given state or with the transition between states in response to stimuli (e.g. triggers and events).

**L5-Elements**

_Elemente:_
- **OperationalArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the Operational perspective.
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.
- **OperationalStateDescription** (`StateMachine`) – A state machine describing the behavior of a OperationalPerformer, depicting how the OperationalPerformer responds to various events and the actions.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
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

## L6 – L6 - Logical Sequence

- Diagrammtyp: `Diagram_Sequence`
- Toolbox: `NAFv4-ADMBw-L6-Toolbox`
- Zweck: Operational Event-Trace Descriptions, sometimes called sequence diagrams, event scenarios or timing diagrams, allow the tracing of interactions between nodes in a scenario or critical sequence of events. The node interactions usually correspond to flows of information but may describe flows of energy, materiel or people specified in the L2, Logical Scenario.

**L6-Elements && Relationships**

_Elemente:_
- **OperationalMessage** (`Message`) – Message for use in an Operational Event-Trace which carries any of the subtypes of OperationalExchange.
- **OperationalRole** (`Part`) – Usage of a OperationalPerformer or OperationalArchitecture in the context of another OperationalPerformer or OperationalArchitecture. Creates a whole-part relationship.
- **ServiceMessage** (`Message`) – Message for use in a Service Event-Trace.
- **ServiceSpecificationRole** (`Part`) – An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

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

## L7 – L7 - Information Model

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L7-Toolbox`
- Zweck: The L7 Viewpoint is used to document the business information. It describes the information that can be exchanged along the logical flows in the architecture, specified in L3 Node Interactions.

**L7-Elements && Relationships**

_Elemente:_
- **DataModel** (`Package`) – A structural specification of data types, showing relationships between them that is devoid of implementation detail. The type of data captured in the DataModel is described using the enumaration DataModelKind (Conceptual,Logical and Physical).
- **InformationElement** (`Class`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable to perform (see IsCapableToPerform).
- **InformationRole** (`Part`) – A usage of InformationElement that exists in the context of an OperationalAsset. It also allows the representation of the whole-part aggregation of InformationElements.

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **ResourceConstraint** (`Class`) – A rule governing the structural or functional aspects of an implementation.
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

## L8 – L8 - Logical Constraints

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L8-Toolbox`
- Zweck: The L8 Viewpoint is used to constrain the logical architecture without forcing a particular solution. L8 is used for rules which are not expressed as behavioural models, interactions or measures of effectiveness, i.e. they are textual statements of requirements that constrain the architecture.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

**Implements Constraints**

_Elemente:_
- **ResourceConstraint** (`Class`) – A rule governing the structural or functional aspects of an implementation.
- **ServicePolicy** (`Class`) – A constraint governing the use of one or more ServiceSpecifications.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.

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

## Lr – Lr - Lines of Development

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-Lr-Toolbox`
- Zweck: The Lr Viewpoint is primarily intended to support the acquisition process across multiple projects or programmes, highlighting dependencies the logical dependencies between capabilities, projects and the integration of all lines of development to achieve a successfully integrated military capability. Use of the Lr Viewpoint should support the management of capability delivery and be aligned with Cr, Capability Roadmap.

**Lr-Actual Projects**

_Elemente:_
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **ActualProjectMilestone** (`Object`) – An event with a start date in a ActualProject from which progress is measured.

_Beziehungen:_
- **ActualProjectConsults** (`Dependency`) – A relation that expresses that a project consults an OrganizationalResource.
- **ActualProjectDependency** (`Dependency`) – Relationship that is a dependency of a actualproject on a actualproject.
- **ActualProjectInforms** (`Dependency`) – A relation that expresses that a project informs an OrganizationalResource.
- **IsAccountableFor** (`Dependency`) – A relation that expresses that an OrganizationalResource is responsible for a resource, service or project in the context of an approval.
- **IsResponsibleFor** (`Dependency`) – A relation that expresses that an OrganizationalResource is responsible for a resource, service or project.
- **MilestoneDependency** (`Dependency`) – A tuple between two ActualProjectMilestones that denotes one ActualProjectMilestone follows from another.
- **OwnedMilestone** (`Dependency`) – Relationship that expresses that actual project has a actual milestone.
- **ProjectMilestoneToProjectTheme** (`Dependency`) – A relationship that expresses which project theme is handled by which project milestone.
- **ProjectSequence** (`Dependency`) – A tuple between two ActualProjects that denotes one ActualProject cannot start before the previous ActualProject is finished.
- **VersionReleased** (`Dependency`) – A relationship that expresses that an actual project milestone releases an versioned element.
- **VersionWithdrawn** (`Dependency`) – A relationship that expresses that an actual project milestone withdraws an versioned element.

**Lr-Project Definition**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **EnterprisePhase** (`Class`) – A current or future state of the wholeLifeEnterprise or another EnterprisePhase.
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.
- **ProjectMilestone** (`Class`) – A type of event in a Project by which progress is measured.
- **ProjectMilestoneRole** (`Part`) – The role played by a ProjectMilestone in the context of a Project.
- **ProjectTheme** (`Part`) – A property of a ProjectMilestone that captures an aspect by which the progress of ActualProjects may be measured.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.

_Beziehungen:_
- **RequiredResource** (`Dependency`) – Relationship that indicates which resources a project milestone requires

**Architecture for Project**

_Elemente:_
- **ArchitecturalDescription** (`Package`) – An Architecture Description is a work product used to express the Architecture of some System Of Interest. It provides executive-level summary information about the architecture description in a consistent form to allow quick reference and comparison between architecture descriptions -- It includes assumptions, constraints, and limitations that may affect high-level decisions relating to an architecture-based work program.

_Beziehungen:_
- **ArchitectureForProject** (`Dependency`) – A relationship that expresses that a architectural description belongs to a actual project.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

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

## L2-L3 – L2-L3 - Logical Concept

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L2-L3-Toolbox`
- Zweck: The L2-L3 Viewpoint is concerned with providing an executive level, scenario-based communication of the architecture purpose, scope and content.

**L2-L3-Elements**

_Elemente:_
- **ConceptRole** (`Part`) – Usage of a ConceptItem in the context of a HighLevelOperationalConcept.
- **HighLevelOperationalConcept** (`Class`) – Describes the Resources and Locations required to meet an operational scenario from an integrated systems point of view. It is used to communicate overall quantitative and qualitative system characteristics to stakeholders

**L2-L3-Relationships**

_Beziehungen:_
- **ArbitraryConnector** (`Dependency`) – Represents a visual indication of a connection used in high level operational concept diagrams.

**L2-L3-Types**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **DataElement** (`Class`) – A formalized representation of data that is managed by or exchanged between resources.
- **InformationElement** (`Class`) – An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are capable to perform (see IsCapableToPerform).
- **Location** (`DataType`) – A specification of the generic area in which a LocationHolder is required to be located.
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **OperationalArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the Operational perspective.
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **Software** (`Class`) – A sub-type of ResourceArtifact that specifies an executable computer program.
- **System** (`Class`) – An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements (INCOSE SE Handbook V4, 2015).

**Measurements**

_Elemente:_
- **ActualCondition** (`Object`) – An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed.
- **ActualEnvironment** (`Object`) – The ActualState that describes the circumstances of an Environment.
- **ActualLocation** (`Object`) – The ActualState that describes a physical location, for example using text to provide an address, Geo-coordinates, etc.
- **Measurement** (`Part`) – A property of an element representing something in the physical world, expressed in amounts of a unit of measure.
- **MeasurementType** (`Class`) – A type of a property representing something in the physical world, expressed in amounts of a unit of measure.

_Beziehungen:_
- **EnvironmentalContext** (`Dependency`) – Relationship that indicates under which condition an measurement counts.
- **OwnsMeasurement** (`Dependency`) – A relationship that expresses which measurement or measurement type an element owns.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Operational Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

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