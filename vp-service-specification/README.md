# Service Specification Viewpoints

Zusammenfassung der Service Specification Viewpoints inklusive Diagrammtypen, Toolboxes sowie erlaubten Elementen und Beziehungen. Detaildaten siehe `service_specification_viewpoints.json`.

| Kennung | Name | Diagrammtyp | Toolbox | Beschreibung |
| --- | --- | --- | --- | --- |
| S1 | S1 - Service Taxonomy | Diagram_Custom | NAFv4-ADMBw-S1-Toolbox | The purpose of the S1 Viewpoint is to provide a governance structure for a Service-Oriented Architecture. Along with S3, Service Interfaces, it specifies a standard library of service specifications for an enterprise, to which service implementers are expected to conform. |
| S2 | S2 - Service Structure | Diagram_Custom | NAFv4-ADMBw-S2-Toolbox | The S2 Viewpoint is concerned with identification and description of how services are structured to create a higher-aggregated service. To provide highlevel views, dependencies to other services, nodes and resources as well as service interfaces and service functions can be represented. |
| S3 | S3 - Service Interfaces | Diagram_Custom | NAFv4-ADMBw-S3-Toolbox | The S3 Viewpoint is concerned with the identification and definition of service interfaces. |
| S4 | S4 - Service Functions | Diagram_Custom | NAFv4-ADMBw-S4-Toolbox | The S4 Viewpoint is the key behavioural specification for services. Equivalent in nature to L4, Logical Activities and P4, Resources Functions, it specifies a set of functions that a service implementation is expected to perform. Implementation of that behaviour is represented in P4, Resource Functions, and L4-P4, Activity to Function Mapping. |
| S5 | S5 - Service States | Diagram_Custom | NAFv4-ADMBw-S5-Toolbox | The S5 Viewpoint is a specification of the allowable states of a service, and the possible transitions between them. This specification constrains how implementations of the service will behave. It is, though, generally considered a good practice to make services stateless - i.e. consumers of a service are not aware of what state the service is in. |
| S6 | S6 - Service Interactions | Diagram_Sequence | NAFv4-ADMBw-S6-Toolbox | Service Interaction Descriptions, sometimes called sequence diagrams, event scenarios or timing diagrams, allow the tracing of interactions between services in a composition or critical sequence of events. |
| S7 | S7 - Service Interface Parameters | Diagram_Custom | NAFv4-ADMBw-S7-Toolbox | Specifies the interfaces that a service provides and uses, defines which services are compatible with which other services. |
| S8 | S8 - Service Policy | Diagram_Custom | NAFv4-ADMBw-S8-Toolbox | The S8 Viewpoint specifies constraints against services to which implementations must conform. |
| Sr | Sr - Service Roadmap | Diagram_Custom | NAFv4-ADMBw-Sr-Toolbox | The Sr Viewpoint supports the Service Audit process by providing a method to identify gaps or duplications in service provision. Sr indicates service lifetime evolutions, which are derived from delivery milestones within acquisition projects. |
| C1-S1 | C1-S1 - Capability to Service Mapping | Diagram_Custom | NAFv4-ADMBw-C1-S1-Toolbox | A C1-S1 Viewpoint presents a simple mapping of services to capabilities, showing which services contribute to which capability. |

## S1 – S1 - Service Taxonomy

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-S1-Toolbox`
- Zweck: The purpose of the S1 Viewpoint is to provide a governance structure for a Service-Oriented Architecture. Along with S3, Service Interfaces, it specifies a standard library of service specifications for an enterprise, to which service implementers are expected to conform.

**S1-Elements && Relationships**

_Elemente:_
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.

_Beziehungen:_
- **ServiceClassification** (`Dependency`) – Relation is used to show that two services have a relationship in the sense of a taxonomy.
- **ServiceSpecificationGeneralization** (`Generalization`) – A ServiceSpecificationGeneralization is a taxonomic relationship between a more general ServiceSpecification and a more specific ServiceSpecification.

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

**Service Policy**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
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

## S2 – S2 - Service Structure

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-S2-Toolbox`
- Zweck: The S2 Viewpoint is concerned with identification and description of how services are structured to create a higher-aggregated service. To provide highlevel views, dependencies to other services, nodes and resources as well as service interfaces and service functions can be represented.

**S2-Service**

_Elemente:_
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.
- **ServiceSpecificationRole** (`Part`) – An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality.

_Beziehungen:_
- **ServiceDependency** (`Dependency`) – Relationship that is a dependency of a service on a service, operational node or resource.

**S2-Dependency to Operational Agent**

_Elemente:_
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.

**S2-Dependency to Resources**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **ResourceInterface** (`Class`) – A declaration that specifies a contract between the ResourcePerformers it is related to and any other ResourcePerformers it can interact with. It is also intended to be an implementation of a specification of an Interface in the Business and/or Service layer.
- **ServiceInterface** (`Class`) – A contract that defines the ServiceMethods and ServiceMessageHandlers that the ServiceSpecification realizes.
- **Software** (`Class`) – A sub-type of ResourceArtifact that specifies an executable computer program.
- **System** (`Class`) – An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements (INCOSE SE Handbook V4, 2015).

_Beziehungen:_
- **IsAccountableFor** (`Dependency`) – A relation that expresses that an OrganizationalResource is responsible for a resource, service or project in the context of an approval.
- **IsResponsibleFor** (`Dependency`) – A relation that expresses that an OrganizationalResource is responsible for a resource, service or project.

**S2-Interface**

_Elemente:_
- **ServiceInterface** (`Class`) – A contract that defines the ServiceMethods and ServiceMessageHandlers that the ServiceSpecification realizes.
- **ServicePort** (`Port`) – An interaction point for a ServiceSpecification through which it can interact with the outside environment and which is defined by a ServiceInterface.

_Beziehungen:_
- **ProvidesServiceFunction** (`Dependency`) – Relationship that expresses that a service function is provided by an interface.

**S2-ServiceFunction**

_Elemente:_
- **ServiceFunction** (`Activity`) – An Activity that describes the abstract behavior of ServiceSpecifications, regardless of the actual implementation.

_Beziehungen:_
- **IsCapableToPerform** (`Abstraction`) – A relationship that says that a capable element performs an activity or action.

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

**Service Policy**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
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

## S3 – S3 - Service Interfaces

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-S3-Toolbox`
- Zweck: The S3 Viewpoint is concerned with the identification and definition of service interfaces.

**S3-Elements && Relationships**

_Elemente:_
- **DataElement** (`Class`) – A formalized representation of data that is managed by or exchanged between resources.
- **DataRole** (`Part`) – A usage of DataElement that exists in the context of an ResourceAsset. It also allows the representation of the whole-part aggregation of DataElements.
- **ServiceInterface** (`Class`) – A contract that defines the ServiceMethods and ServiceMessageHandlers that the ServiceSpecification realizes.
- **ServicePort** (`Port`) – An interaction point for a ServiceSpecification through which it can interact with the outside environment and which is defined by a ServiceInterface.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.

_Beziehungen:_
- **ServiceConnector** (`Connector`) – A channel for exchange between two ServiceSpecifications. Where one acts as the consumer of the other.

**Service Policy**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
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

## S4 – S4 - Service Functions

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-S4-Toolbox`
- Zweck: The S4 Viewpoint is the key behavioural specification for services. Equivalent in nature to L4, Logical Activities and P4, Resources Functions, it specifies a set of functions that a service implementation is expected to perform. Implementation of that behaviour is represented in P4, Resource Functions, and L4-P4, Activity to Function Mapping.

**S4-Elements && Relationships**

_Elemente:_
- **ServiceFunction** (`Activity`) – An Activity that describes the abstract behavior of ServiceSpecifications, regardless of the actual implementation.
- **ServiceFunctionAction** (`Action`) – A call of a ServiceFunction in the context of another ServiceFunction.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.
- **ServiceSpecificationRole** (`Part`) – An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality.

_Beziehungen:_
- **IsCapableToPerform** (`Abstraction`) – A relationship that says that a capable element performs an activity or action.
- **PerformsInContext** (`Abstraction`) – A relationship that says that a role performs an activity or action. It indicates that the action can be carried out by the role when used in a specific context or configuration.

**Service Policy**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
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

## S5 – S5 - Service States

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-S5-Toolbox`
- Zweck: The S5 Viewpoint is a specification of the allowable states of a service, and the possible transitions between them. This specification constrains how implementations of the service will behave. It is, though, generally considered a good practice to make services stateless - i.e. consumers of a service are not aware of what state the service is in.

**S5-Elements**

_Elemente:_
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.
- **ServiceStateDescription** (`StateMachine`) – A state machine descripting the behavior of a ServiceSpecification, depicting how the ServiceSpecification responds to various events and the actions.

**Service Policy**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
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

## S6 – S6 - Service Interactions

- Diagrammtyp: `Diagram_Sequence`
- Toolbox: `NAFv4-ADMBw-S6-Toolbox`
- Zweck: Service Interaction Descriptions, sometimes called sequence diagrams, event scenarios or timing diagrams, allow the tracing of interactions between services in a composition or critical sequence of events.

**S6-Elements && Relationships**

_Elemente:_
- **OperationalMessage** (`Message`) – Message for use in an Operational Event-Trace which carries any of the subtypes of OperationalExchange.
- **OperationalRole** (`Part`) – Usage of a OperationalPerformer or OperationalArchitecture in the context of another OperationalPerformer or OperationalArchitecture. Creates a whole-part relationship.
- **ResourceMessage** (`Message`) – Message for use in an Resource Event-Trace which carries any of the subtypes of ResourceExchange.
- **ResourceRole** (`Part`) – Usage of a ResourcePerformer in the context of another ResourcePerformer. Creates a whole-part relationship.
- **ServiceMessage** (`Message`) – Message for use in a Service Event-Trace.
- **ServiceSpecificationRole** (`Part`) – An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality.

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

## S7 – S7 - Service Interface Parameters

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-S7-Toolbox`
- Zweck: Specifies the interfaces that a service provides and uses, defines which services are compatible with which other services.

**S7-Elements && Relationships**

_Elemente:_
- **ServiceFunction** (`Activity`) – An Activity that describes the abstract behavior of ServiceSpecifications, regardless of the actual implementation.
- **ServiceInterface** (`Class`) – A contract that defines the ServiceMethods and ServiceMessageHandlers that the ServiceSpecification realizes.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.

_Beziehungen:_
- **ProvidesServiceFunction** (`Dependency`) – Relationship that expresses that a service function is provided by an interface.

**Service Policy**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
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

## S8 – S8 - Service Policy

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-S8-Toolbox`
- Zweck: The S8 Viewpoint specifies constraints against services to which implementations must conform.

**Service Policy**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **ServicePolicy** (`Class`) – A constraint governing the use of one or more ServiceSpecifications.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

**Implements Constraints**

_Elemente:_
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **ResourceConstraint** (`Class`) – A rule governing the structural or functional aspects of an implementation.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.

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

## Sr – Sr - Service Roadmap

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-Sr-Toolbox`
- Zweck: The Sr Viewpoint supports the Service Audit process by providing a method to identify gaps or duplications in service provision. Sr indicates service lifetime evolutions, which are derived from delivery milestones within acquisition projects.

**Sr-Project**

_Elemente:_
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **ActualProjectMilestone** (`Object`) – An event with a start date in a ActualProject from which progress is measured.
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.
- **ProjectMilestone** (`Class`) – A type of event in a Project by which progress is measured.
- **ProjectMilestoneRole** (`Part`) – The role played by a ProjectMilestone in the context of a Project.

_Beziehungen:_
- **ActualProjectDependency** (`Dependency`) – Relationship that is a dependency of a actualproject on a actualproject.
- **IsAccountableFor** (`Dependency`) – A relation that expresses that an OrganizationalResource is responsible for a resource, service or project in the context of an approval.
- **IsResponsibleFor** (`Dependency`) – A relation that expresses that an OrganizationalResource is responsible for a resource, service or project.
- **MilestoneDependency** (`Dependency`) – A tuple between two ActualProjectMilestones that denotes one ActualProjectMilestone follows from another.
- **OwnedMilestone** (`Dependency`) – Relationship that expresses that actual project has a actual milestone.
- **ProjectMilestoneToProjectTheme** (`Dependency`) – A relationship that expresses which project theme is handled by which project milestone.
- **ProjectSequence** (`Dependency`) – A tuple between two ActualProjects that denotes one ActualProject cannot start before the previous ActualProject is finished.
- **RequiredResource** (`Dependency`) – Relationship that indicates which resources a project milestone requires
- **VersionReleased** (`Dependency`) – A relationship that expresses that an actual project milestone releases an versioned element.
- **VersionWithdrawn** (`Dependency`) – A relationship that expresses that an actual project milestone withdraws an versioned element.

**Sr-Services**

_Elemente:_
- **ActualService** (`Object`) – An individual ServiceSpecification.
- **ProvidedServiceLevel** (`Object`) – A sub type of ActualService that details a specific service level delivered by the provider.
- **RequiredServiceLevel** (`Object`) – A sub type of ActualService that details a specific service level required of the provider.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.

_Beziehungen:_
- **NeedsService** (`Dependency`) – A relation that expresses that a project needs a service

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

## C1-S1 – C1-S1 - Capability to Service Mapping

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-C1-S1-Toolbox`
- Zweck: A C1-S1 Viewpoint presents a simple mapping of services to capabilities, showing which services contribute to which capability.

**C1-S1-Elements && Relationships**

_Elemente:_
- **Capability** (`Class`) – A high level specification of the enterprise's ability to execute a specified course of action.
- **Environment** (`Class`) – A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using EnvironmentKind.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.

_Beziehungen:_
- **EnvironmentalCondition** (`Dependency`) – Relationship that indicates under which environment an exhibits-relationship takes place.
- **Exhibits** (`Abstraction`) – A tuple that exists between a CapableElement and a Capability that it meets under specific environmental conditions.

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