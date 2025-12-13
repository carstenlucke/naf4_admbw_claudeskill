# Physical Resource Specification Viewpoints

Übersicht über die Physical Resource Specification Viewpoints inkl. Diagrammtypen, Toolboxes, Elementen und Beziehungen. Detaildaten siehe `physical_resource_specification_viewpoints.json`.

| Kennung | Name | Diagrammtyp | Toolbox | Beschreibung |
| --- | --- | --- | --- | --- |
| P1 | P1 - Resource Types | Diagram_Custom | NAFv4-ADMBw-P1-Toolbox | The P1 Viewpoint collects together all the Resource Types in the architecture together with a depiction of their performance characteristics. P1 also provides a summary of the technologies and competencies that impact on the Resources that constitute the architecture. |
| P2 | P2 - Resource Structure | Diagram_Custom | NAFv4-ADMBw-P2-Toolbox | The P2 Viewpoint links together the operational and physical architecture viewpoints by depicting how types of Resource are structured and interact to realize the logical architecture specified in L2, Logical Scenario. The P2 Viewpoint may represent the realization of a requirement specified in a L2 (i.e. in a “to-be” architecture) and so there may be many alternative Resource viewpoint suites that could realize the operational requirement. Alternatively, in an “as-is” architecture, a L2 may just be a simplified, logical representation of the P2 Viewpoint to allow communication of key information flows to non-technical stakeholders. |
| P3 | P3 - Resource Connectivity | Diagram_Custom | NAFv4-ADMBw-P3-Toolbox | The networks and pathways documented in a P3 Viewpoint represent the physical implementation of the logical flows identified in a L2, Logical Scenario, or L3, Node Interactions View. |
| P4 | P4 - Resource Functions | Diagram_Custom | NAFv4-ADMBw-P4-Toolbox | The Functionality Description provides detailed information regarding the allocation of functions to resources, and flows between Resource Functions. The P4 Viewpoint is the Physical Resource counterpart to the L4 Logical Activities Viewpoint. |
| P5 | P5 - Resource States | Diagram_Custom | NAFv4-ADMBw-P5-Toolbox | The P5 Viewpoint identifies the states a Resource can be, the allowable changes between those states, and the stimuli (e.g. triggers and events) that cause the state changes. |
| P6 | P6 - Resource Sequence | Diagram_Sequence | NAFv4-ADMBw-P6-Toolbox | The P6 Viewpoint is valuable for moving to the next level of detail from the initial solution design, to help define a sequence of functions and Resource Interactions, and to ensure that each participating Resource or Port has the necessary information, at the right time, in order to perform its assigned functionality. |
| P7 | P7 -  Data Model | Diagram_Custom | NAFv4-ADMBw-P7-Toolbox | The P7 Viewpoint is one of the architectural products closest to actual system design in the NAF. It is used to describe how the information represented in the L7 Logical Data Model Viewpoint is implemented. |
| P8 | P8 - Resource Constraints | Diagram_Custom | NAFv4-ADMBw-P8-Toolbox | The P8 Viewpoint describes constraints on the Resources, Resource Functions, data and communications that make up a Physical Architecture. |
| Pr | Pr - Configuration Management | Diagram_Custom | NAFv4-ADMBw-Pr-Toolbox | The Pr Viewpoint provides an overview of how Resource Assets change over time (note that NAF v3.1 only allowed for Capability Configurations whereas now this is opened up to all Resource Types). It shows the structure of different versions of Resource Assets (usually Capability Configurations or Service Implementations) mapped against a timeline. |
| L4-P4 | L4-P4 - Activity To Function Mapping | Diagram_Custom | NAFv4-ADMBw-L4-P4-Toolbox | The L4-P4 Viewpoint depicts the mapping of Resource Functions (and optionally, the resources that provide them) to operational activities and/or service functions. For operational activities it thus identifies the transformation of an operational need into a purposeful action performed by a system or solution. For service functions it provides the link between the services used at the operational level and the specific Resource Functions provided by the resources supporting the services. |

## P1 – P1 - Resource Types

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-P1-Toolbox`
- Zweck: The P1 Viewpoint collects together all the Resource Types in the architecture together with a depiction of their performance characteristics. P1 also provides a summary of the technologies and competencies that impact on the Resources that constitute the architecture.

**P1-Elements && Relationships**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **Energy** (`Class`) – A representation of any kind of energy.
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **ResourceInterface** (`Class`) – A declaration that specifies a contract between the ResourcePerformers it is related to and any other ResourcePerformers it can interact with. It is also intended to be an implementation of a specification of an Interface in the Business and/or Service layer.
- **Software** (`Class`) – A sub-type of ResourceArtifact that specifies an executable computer program.
- **System** (`Class`) – An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements (INCOSE SE Handbook V4, 2015).
- **Technology** (`Class`) – A sub type of ResourceArtifact that indicates a technology domain, i.e. nuclear, mechanical, electronic, mobile telephony etc.

_Beziehungen:_
- **PropertySetGeneralisation** (`Generalization`) – A PropertySetGeneralization is a taxonomic relationship between a more general PropertySet and a more specific PropertySet.

**P1-Forecast**

_Elemente:_
- **ActualEnterprisePhase** (`Object`) – The ActualState that describes the phase of an Enterprise endeavor.
- **EnterprisePhase** (`Class`) – A current or future state of the wholeLifeEnterprise or another EnterprisePhase.

_Beziehungen:_
- **Forecast** (`Dependency`) – A tuple that specifies a transition from one Asset, Standard, Competence to another future one. It is related to an ActualEnterprisePhase to give it a temporal context.
- **ForecastPeriod** (`Dependency`) – Planning phase for which the forecast is valid.

**P1-Organizations**

_Elemente:_
- **Competence** (`Class`) – A specific set of abilities defined by knowledge, skills and aptitude.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).

_Beziehungen:_
- **RequiresCompetence** (`Abstraction`) – A tuple that asserts that an ActualOrganizationalResource is required to have a specific set of Competencies.

**P1-Implements**

_Elemente:_
- **ActualResource** (`Object`) – Role in an Organisation, where the role carries the authority to undertake a function - through the ActualOrganizationalResource given the role has the responsibility.
- **ActualService** (`Object`) – An individual ServiceSpecification.
- **ProvidedServiceLevel** (`Object`) – A sub type of ActualService that details a specific service level delivered by the provider.
- **RequiredServiceLevel** (`Object`) – A sub type of ActualService that details a specific service level required of the provider.

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.

**P1-StoredIn**

_Elemente:_
- **DataElement** (`Class`) – A formalized representation of data that is managed by or exchanged between resources.
- **PaperForm** (`Class`) – Form is a digitized or digitizable document, for example a scanned document.

_Beziehungen:_
- **DataElementStoredIn** (`Dependency`) – Relation says that a data is stored in software.
- **FormStoredIn** (`Dependency`) – Relation states that a digital form is stored in software.

**P1-Services**

_Elemente:_
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.

_Beziehungen:_
- **ServiceProvision** (`Abstraction`) – An assertion that a Resource delivers a Service to a specified ServiceLevel.

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

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
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

## P2 – P2 - Resource Structure

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-P2-Toolbox`
- Zweck: The P2 Viewpoint links together the operational and physical architecture viewpoints by depicting how types of Resource are structured and interact to realize the logical architecture specified in L2, Logical Scenario. The P2 Viewpoint may represent the realization of a requirement specified in a L2 (i.e. in a “to-be” architecture) and so there may be many alternative Resource viewpoint suites that could realize the operational requirement. Alternatively, in an “as-is” architecture, a L2 may just be a simplified, logical representation of the P2 Viewpoint to allow communication of key information flows to non-technical stakeholders.

**P2-Elements && Relationships**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **NaturalResource** (`Class`) – Type of physical resource that occurs in nature.
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **ResourceRole** (`Part`) – Usage of a ResourcePerformer in the context of another ResourcePerformer. Creates a whole-part relationship.
- **Software** (`Class`) – A sub-type of ResourceArtifact that specifies an executable computer program.
- **System** (`Class`) – An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements (INCOSE SE Handbook V4, 2015).

_Beziehungen:_
- **HostedOn** (`Dependency`) – Relation states that hardware (virtualized) or software is hosted on a virtualized platform or physical hardware.
- **ResourceDependency** (`Dependency`) – Relationship that is a dependency of a resource on a resource.

**P2-Resource Exchange **

_Elemente:_
- **DataElement** (`Class`) – A formalized representation of data that is managed by or exchanged between resources.
- **DataRole** (`Part`) – A usage of DataElement that exists in the context of an ResourceAsset. It also allows the representation of the whole-part aggregation of DataElements.
- **Energy** (`Class`) – A representation of any kind of energy.
- **GeoPoliticalExtentType** (`DataType`) – A geospatial extent whose boundaries are defined by declaration or agreement by political parties.

_Beziehungen:_
- **Control** (`InformationFlow`) – A type of ResourceExchange that asserts that one PhysicalResource controls another PhysicalResource (i.e. the driver of a vehicle controlling the vehicle speed or direction).
- **ResourceExchange** (`InformationFlow`) – Asserts that a flow can exist between ResourcePerformers (i.e. flows of data, people, material, or energy).

**P2-Organizations**

_Elemente:_
- **Competence** (`Class`) – A specific set of abilities defined by knowledge, skills and aptitude.
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **PostRole** (`Part`) – A usage of a post in the context of another OrganizationalResource. Creates a whole-part relationship.
- **SubOrganization** (`Part`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).

_Beziehungen:_
- **Command** (`InformationFlow`) – A type of ResourceExchange that asserts that one OrganizationalResource commands another.
- **CompetenceForRole** (`Dependency`) – A tuple used to associate an organizational role with a specific set of required competencies.

**P2-Project && Resource**

_Elemente:_
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **Function** (`Activity`) – An Activity which is specified in the context to the ResourcePerformer (human or machine) that IsCapableToPerform it.

_Beziehungen:_
- **ActualProjectConsults** (`Dependency`) – A relation that expresses that a project consults an OrganizationalResource.
- **ActualProjectInforms** (`Dependency`) – A relation that expresses that a project informs an OrganizationalResource.
- **IsAccountableFor** (`Dependency`) – A relation that expresses that an OrganizationalResource is responsible for a resource, service or project in the context of an approval.
- **IsResponsibleFor** (`Dependency`) – A relation that expresses that an OrganizationalResource is responsible for a resource, service or project.
- **NeedsModificationOf** (`Dependency`) – Relation stats that a project makes adjustments to a resource.
- **NeedsResource** (`Dependency`) – Relation stats that a project needs a resource.
- **ProjectProvidesFunction** (`Dependency`) – Relation stats that a project realizes a function.
- **ProjectSupportActivity** (`Dependency`) – Relation stats that a project supports an activity.
- **Responsible** (`Dependency`) – Relation states that a project is responsible for a service or a material resource.

**P2-Services**

_Elemente:_
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.
- **ServiceSpecificationRole** (`Part`) – An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality.

_Beziehungen:_
- **ResourceToServiceDependency** (`Dependency`) – Relation states that a resource is dependent on a service.
- **ServiceProvision** (`Abstraction`) – An assertion that a Resource delivers a Service to a specified ServiceLevel.

**P2-Implements**

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

**Environment && Location**

_Elemente:_
- **ActualEnvironment** (`Object`) – The ActualState that describes the circumstances of an Environment.
- **ActualLocation** (`Object`) – The ActualState that describes a physical location, for example using text to provide an address, Geo-coordinates, etc.
- **Environment** (`Class`) – A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using EnvironmentKind.
- **Location** (`Class`) – A specification of the generic area in which a LocationHolder is required to be located.

_Beziehungen:_
- **LocationType** (`Dependency`) – A relationship that expresses which location is assigned to a location holder.
- **PhysicalLocation** (`Dependency`) – A relationship that expresses that a location holder operates in an actual location.
- **RequiredEnvironment** (`Dependency`) – A relationship that expresses that a location holder operates under specific environmental conditions.

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
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

## P3 – P3 - Resource Connectivity

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-P3-Toolbox`
- Zweck: The networks and pathways documented in a P3 Viewpoint represent the physical implementation of the logical flows identified in a L2, Logical Scenario, or L3, Node Interactions View.

**P3-Elements && Dependency**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ResourceArtifact** (`Class`) – A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).
- **ResourceRole** (`Part`) – Usage of a ResourcePerformer in the context of another ResourcePerformer. Creates a whole-part relationship.
- **Software** (`Class`) – A sub-type of ResourceArtifact that specifies an executable computer program.
- **System** (`Class`) – An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements (INCOSE SE Handbook V4, 2015).

_Beziehungen:_
- **ResourceDependency** (`Dependency`) – Relationship that is a dependency of a resource on a resource.

**P3-Connector && ResourcePort**

_Elemente:_
- **ResourceInterface** (`Class`) – A declaration that specifies a contract between the ResourcePerformers it is related to and any other ResourcePerformers it can interact with. It is also intended to be an implementation of a specification of an Interface in the Business and/or Service layer.
- **ResourcePort** (`Port`) – An interaction point for a ResourcePerformer through which it can interact with the outside environment and which is defined by a ResourceInterface.

_Beziehungen:_
- **BoundaryCondition** (`Dependency`) – A relationship that expresses which environment is relevant to an resource exchange.
- **ResourceConnector** (`Connector`) – A channel for exchange between two ResourceRoles.

**P3-Protocols**

_Elemente:_
- **Protocol** (`Class`) – A Standard for communication over a network. Protocols may be composite, represented as a ProtocolStack made up of ProtocolLayers.
- **ProtocolLayer** (`Part`) – Usage of a Protocol in the context of another Protocol. Creates a whole-part relationship.
- **Protocolstack** (`Class`) – A sub type of Protocol that contains the ProtocolLayers, defining a complete stack.
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.
- **ImplementsProtocol** (`Dependency`) – A relationship that expresses which protocol implements an architectural element.

**P3-Exchanges**

_Elemente:_
- **DataElement** (`Class`) – A formalized representation of data that is managed by or exchanged between resources.
- **DataRole** (`Part`) – A usage of DataElement that exists in the context of an ResourceAsset. It also allows the representation of the whole-part aggregation of DataElements.
- **ResourceSignal** (`Signal`) – A property of an element representing something in the physical world, expressed in amounts of a unit of measure.

_Beziehungen:_
- **Control** (`InformationFlow`) – A type of ResourceExchange that asserts that one PhysicalResource controls another PhysicalResource (i.e. the driver of a vehicle controlling the vehicle speed or direction).
- **ResourceExchange** (`InformationFlow`) – Asserts that a flow can exist between ResourcePerformers (i.e. flows of data, people, material, or energy).

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **ResourceConstraint** (`Class`) – A rule governing the structural or functional aspects of an implementation.
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

## P4 – P4 - Resource Functions

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-P4-Toolbox`
- Zweck: The Functionality Description provides detailed information regarding the allocation of functions to resources, and flows between Resource Functions. The P4 Viewpoint is the Physical Resource counterpart to the L4 Logical Activities Viewpoint.

**P4-Functions**

_Elemente:_
- **DataElement** (`Class`) – A formalized representation of data that is managed by or exchanged between resources.
- **FunctionAction** (`Action`) – A call of a Function indicating that the Function is performed by a ResourceRole in a specific context.

_Beziehungen:_
- **FunctionControlFlow** (`ControlFlow`) – An ActivityEdge that shows the flow of control between FunctionActions.
- **FunctionObjectFlow** (`ObjectFlow`) – An ActivityEdge that shows the flow of Resources (objects/data) between FunctionActions.

**P4-Resource Function Mapping**

_Elemente:_
- **Function** (`Activity`) – An Activity which is specified in the context to the ResourcePerformer (human or machine) that IsCapableToPerform it.

_Beziehungen:_
- **IsCapableToPerform** (`Abstraction`) – A relationship that says that a capable element performs an activity or action.
- **PerformsInContext** (`Abstraction`) – A relationship that says that a role performs an activity or action. It indicates that the action can be carried out by the role when used in a specific context or configuration.

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

**Affecte && Subject**

_Beziehungen:_
- **AffectedFunctions** (`Dependency`) – A relationship that expresses which function is affected by a resource.
- **FunctionSubject** (`Dependency`) – A relationship that expresses that a function uses certain resources.

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
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

## P5 – P5 - Resource States

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-P5-Toolbox`
- Zweck: The P5 Viewpoint identifies the states a Resource can be, the allowable changes between those states, and the stimuli (e.g. triggers and events) that cause the state changes.

**P5-Elements**

_Elemente:_
- **ResourceStateDescription** (`StateMachine`) – A state machine describing the behavior of a ResourcePerformer, depicting how the ResourcePerformer responds to various events and the actions.

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
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

## P6 – P6 - Resource Sequence

- Diagrammtyp: `Diagram_Sequence`
- Toolbox: `NAFv4-ADMBw-P6-Toolbox`
- Zweck: The P6 Viewpoint is valuable for moving to the next level of detail from the initial solution design, to help define a sequence of functions and Resource Interactions, and to ensure that each participating Resource or Port has the necessary information, at the right time, in order to perform its assigned functionality.

**P6-Elements**

_Elemente:_
- **ResourceMessage** (`Message`) – Message for use in an Resource Event-Trace which carries any of the subtypes of ResourceExchange.
- **ResourceRole** (`Part`) – Usage of a ResourcePerformer in the context of another ResourcePerformer. Creates a whole-part relationship.
- **ServiceMessage** (`Message`) – Message for use in a Service Event-Trace.
- **ServiceSpecificationRole** (`Part`) – An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality.

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
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

## P7 – P7 -  Data Model

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-P7-Toolbox`
- Zweck: The P7 Viewpoint is one of the architectural products closest to actual system design in the NAF. It is used to describe how the information represented in the L7 Logical Data Model Viewpoint is implemented.

**P7-Elements && Relationships**

_Elemente:_
- **DataElement** (`Class`) – A formalized representation of data that is managed by or exchanged between resources.
- **DataModel** (`Package`) – A structural specification of data types, showing relationships between them that is devoid of implementation detail. The type of data captured in the DataModel is described using the enumaration DataModelKind (Conceptual,Logical and Physical).
- **DataRole** (`Part`) – A usage of DataElement that exists in the context of an ResourceAsset. It also allows the representation of the whole-part aggregation of DataElements.

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.

**Conforms To Standard**

_Elemente:_
- **Standard** (`Class`) – A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

_Beziehungen:_
- **ConformsTo** (`Dependency`) – A relationship that expresses that an UAFElement conforms to a standard.

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **ResourceConstraint** (`Class`) – A rule governing the structural or functional aspects of an implementation.
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

## P8 – P8 - Resource Constraints

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-P8-Toolbox`
- Zweck: The P8 Viewpoint describes constraints on the Resources, Resource Functions, data and communications that make up a Physical Architecture.

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
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

**Implements Constraints**

_Elemente:_
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **ServicePolicy** (`Class`) – A constraint governing the use of one or more ServiceSpecifications.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.

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

## Pr – Pr - Configuration Management

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-Pr-Toolbox`
- Zweck: The Pr Viewpoint provides an overview of how Resource Assets change over time (note that NAF v3.1 only allowed for Capability Configurations whereas now this is opened up to all Resource Types). It shows the structure of different versions of Resource Assets (usually Capability Configurations or Service Implementations) mapped against a timeline.

**Successor of**

_Beziehungen:_
- **SuccessorOf** (`Dependency`) – A relationship between two elements that indicates that one element is the successor of the other.

**Pr-Configuration Management**

_Elemente:_
- **VersionOfConfiguration** (`Part`) – A property of a WholeLifeConfiguration, used in version control of a VersionedElement. It asserts that a VersionedElement is a version of a WholeLifeConfiguration.
- **WholeLifeConfiguration** (`Class`) – A set of VersionedElements.

_Beziehungen:_
- **VersionSuccession** (`Dependency`) – A tuple between two VersionOfConfigurations that denotes that one VersionOfConfiguration follows from another.

**Pr-Project Management**

_Elemente:_
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **ActualProjectMilestone** (`Object`) – An event with a start date in a ActualProject from which progress is measured.
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.
- **ProjectMilestone** (`Class`) – A type of event in a Project by which progress is measured.
- **ProjectMilestoneRole** (`Part`) – The role played by a ProjectMilestone in the context of a Project.

_Beziehungen:_
- **ActualProjectDependency** (`Dependency`) – Relationship that is a dependency of a actualproject on a actualproject.
- **MilestoneDependency** (`Dependency`) – A tuple between two ActualProjectMilestones that denotes one ActualProjectMilestone follows from another.
- **OwnedMilestone** (`Dependency`) – Relationship that expresses that actual project has a actual milestone.
- **ProjectMilestoneToProjectTheme** (`Dependency`) – A relationship that expresses which project theme is handled by which project milestone.
- **ProjectSequence** (`Dependency`) – A tuple between two ActualProjects that denotes one ActualProject cannot start before the previous ActualProject is finished.
- **RequiredResource** (`Dependency`) – Relationship that indicates which resources a project milestone requires
- **VersionReleased** (`Dependency`) – A relationship that expresses that an actual project milestone releases an versioned element.
- **VersionWithdrawn** (`Dependency`) – A relationship that expresses that an actual project milestone withdraws an versioned element.

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
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

## L4-P4 – L4-P4 - Activity To Function Mapping

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-L4-P4-Toolbox`
- Zweck: The L4-P4 Viewpoint depicts the mapping of Resource Functions (and optionally, the resources that provide them) to operational activities and/or service functions. For operational activities it thus identifies the transformation of an operational need into a purposeful action performed by a system or solution. For service functions it provides the link between the services used at the operational level and the specific Resource Functions provided by the resources supporting the services.

**L4-P4-Relationships**

_Beziehungen:_
- **Implements** (`Abstraction`) – A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivities to the Functions that implement them) in the lower level of abstraction.
- **IsCapableToPerform** (`Abstraction`) – A relationship that says that a capable element performs an activity or action.
- **PerformsInContext** (`Abstraction`) – A relationship that says that a role performs an activity or action. It indicates that the action can be carried out by the role when used in a specific context or configuration.
- **ServiceProvision** (`Abstraction`) – An assertion that a Resource delivers a Service to a specified ServiceLevel.

**Resource Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
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