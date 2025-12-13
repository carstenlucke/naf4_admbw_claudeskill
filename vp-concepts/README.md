# Concept Viewpoints

Übersicht über die Concept Viewpoints inkl. Diagrammtypen, Toolboxes sowie erlaubte Elemente und Beziehungen. Detaildaten siehe `concept_viewpoints.json`.

| Kennung | Name | Diagrammtyp | Toolbox | Beschreibung |
| --- | --- | --- | --- | --- |
| C1 | C1 - Capability Taxonomy | Diagram_Custom | NAFv4-ADMBw-C1-Toolbox | The C1 Viewpoint specifies all the capabilities that are referenced throughout one or more architectures – i.e. one C1 may provide the definitive list of capabilities for a number of logical and resource architectures. The capabilities may be organised into specialisation hierarchies (taxonomies). Measures of Effectiveness (MoE) may be specified for each capability. Note that MoEs are inherited down a capability taxonomy. |
| C2 | C2 - Enterprise Vision | Diagram_Custom | NAFv4-ADMBw-C2-Toolbox | The purpose of the C2 Viewpoint is to provide a strategic context for the capabilities described in the architecture and to specify the scope for the architecture. The C2 Viewpoint is high-level and describes the vision, goals, enduring tasks and capabilities using terminology that is easily understood by non-technical readers. |
| C3 | C3 - Capability Dependencies | Diagram_Custom | NAFv4-ADMBw-C3-Toolbox | The C3 Viewpoint is intended to provide a means of analysing the dependencies between capabilities and between capability clusters. The composition of capabilities (into clusters) is logical and the purpose of the clusters is to guide enterprise management. |
| C4 | C4 - Standard Processes | Diagram_Custom | NAFv4-ADMBw-C4-Toolbox | The C4 Viewpoint specifies Standard Operational Activities that can be re-used across multiple logical architectures (e.g. in L4, Logical Activities). |
| C5 | C5 - Effects | Diagram_Custom | NAFv4-ADMBw-C5-Toolbox | The purpose of the C5 Viewpoint is to describe the operational effect of the capabilities, activities and services according to the expected goals. The C5 Viewpoint is high-level description that should be easily understood by non-technical readers. |
| C7 | C7 - Performance Parameters | Diagram_Custom | NAFv4-ADMBw-C7-Toolbox | In the C7 Viewpoint the capability requirements (and existing capabilities) can be expressed in terms of Measures of Effectiveness (MoEs). These are high-level metrics used to judge the level of capability. |
| C8 | C8 - Planning Assumptions | Diagram_Custom | NAFv4-ADMBw-C8-Toolbox | The C8 Viewpoint is concerned with identification and description of assumptions that have been made for the implementation of capabilities. Assumptions can be expressed by means of requirements. |
| Cr | Cr - Capability Roadmap | Diagram_Custom | NAFv4-ADMBw-Cr-Toolbox | The Cr Viewpont supports the Capability Audit process by providing a method to identify gaps or duplications in capability provision. Cr indicates capability increments, which are derived from delivery milestones within acquisition projects. |

## C1 – C1 - Capability Taxonomy

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-C1-Toolbox`
- Zweck: The C1 Viewpoint specifies all the capabilities that are referenced throughout one or more architectures – i.e. one C1 may provide the definitive list of capabilities for a number of logical and resource architectures. The capabilities may be organised into specialisation hierarchies (taxonomies). Measures of Effectiveness (MoE) may be specified for each capability. Note that MoEs are inherited down a capability taxonomy.

**C1-Elements && Relationships**

_Elemente:_
- **Capability** (`Class`) – A high level specification of the enterprise's ability to execute a specified course of action.

_Beziehungen:_
- **CapabilityGeneralization** (`Generalization`) – A CapabilityGeneralization is a taxonomic relationship between a more general Capability and a more specific Capability.

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

**Strategic Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

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

## C2 – C2 - Enterprise Vision

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-C2-Toolbox`
- Zweck: The purpose of the C2 Viewpoint is to provide a strategic context for the capabilities described in the architecture and to specify the scope for the architecture. The C2 Viewpoint is high-level and describes the vision, goals, enduring tasks and capabilities using terminology that is easily understood by non-technical readers.

**C2-EnduringTask**

_Elemente:_
- **ActualEnduringTask** (`Object`) – An actual undertaking recognized by an enterprise as being essential to achieving its goals - i.e. a strategic specification of what the enterprise does.
- **EnduringTask** (`Class`) – A type of template behavior recognized by an enterprise as being essential to achieving its goals - i.e. a template for a strategic specification of what the enterprise does.

_Beziehungen:_
- **CapabilityForTask** (`Abstraction`) – A tuple that asserts that a Capability is required in order for an Enterprise to conduct a phase of an EnduringTask.
- **StatementTask** (`Dependency`) – A relationship that expresses that an actual enterprise phase fulfills a actual enduring task.

**C2-Enterprise**

_Elemente:_
- **ActualEnterprisePhase** (`Object`) – The ActualState that describes the phase of an Enterprise endeavor.
- **EnterpriseGoal** (`Class`) – A statement about a state or condition of the enterprise to be brought about or sustained through appropriate Means. An EnterpriseGoal amplifies an EnterpriseVision that is, it indicates what must be satisfied on a continuing basis to effectively attain the EnterpriseVision.
- **EnterprisePhase** (`Class`) – A current or future state of the wholeLifeEnterprise or another EnterprisePhase.
- **EnterpriseVision** (`Class`) – A Vision describes the future state of the enterprise, without regard to how it is to be achieved.
- **OperationalActivity** (`Activity`) – An Activity that captures a logical process, specified independently of how the process is carried out.
- **OperationalArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the Operational perspective.
- **OperationalPerformer** (`Class`) – A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources.
- **ResourceArchitecture** (`Class`) – A type used to denote a model of the Architecture, described from the ResourcePerformer perspective.
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.
- **TemporalPart** (`Part`) – A current or future state of the wholeLifeEnterprise or another EnterprisePhase.
- **WholeLifeEnterprise** (`Class`) – A WholeLifeEnterprise is a purposeful endeavor of any size involving people, organizations and supporting systems. It is made up of TemporalParts and StructuralParts.

_Beziehungen:_
- **AlignsWithGoal** (`Dependency`) – A relationship that expresses that an element is aligned with a goal.
- **GoalForActualEnterprisePhase** (`Dependency`) – A relationship that expresses which actual enterprisephase implements an enterprisegoal.
- **OperationalArchitectureOfEnterprisePhase** (`Dependency`) – Relationship that says that in a actual enterprisephase an operational architecture is valid.
- **VisionForActualEnterprisePhase** (`Dependency`) – A relationship that expresses which actual enterprisephase implements an enterprisevision.

**C2-Exhibits**

_Elemente:_
- **Capability** (`Class`) – A high level specification of the enterprise's ability to execute a specified course of action.
- **Environment** (`Class`) – A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using EnvironmentKind.

_Beziehungen:_
- **EnvironmentalCondition** (`Dependency`) – Relationship that indicates under which environment an exhibits-relationship takes place.
- **Exhibits** (`Abstraction`) – A tuple that exists between a CapableElement and a Capability that it meets under specific environmental conditions.

**Strategic Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

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

**Physical Architecture Of Enterprise Phase**

_Beziehungen:_
- **PhysicalArchitectureOfEnterprisePhase** (`Dependency`) – A relationship that expresses that an actual enterprise phase has resource architectures.

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

## C3 – C3 - Capability Dependencies

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-C3-Toolbox`
- Zweck: The C3 Viewpoint is intended to provide a means of analysing the dependencies between capabilities and between capability clusters. The composition of capabilities (into clusters) is logical and the purpose of the clusters is to guide enterprise management.

**C3-Capability**

_Elemente:_
- **Capability** (`Class`) – A high level specification of the enterprise's ability to execute a specified course of action.

_Beziehungen:_
- **CapabilityDependency** (`Dependency`) – A tuple that asserts that one Capability is dependent from another.

**C3-CapabilityRole**

_Elemente:_
- **CapabilityRole** (`Part`) – A high level specification of the enterprise's ability to execute a specified course of action.

_Beziehungen:_
- **CapabilityRoleDependency** (`Dependency`) – A tuple that asserts that one CapabilityRole is dependent from another.

**Strategic Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

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

## C4 – C4 - Standard Processes

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-C4-Toolbox`
- Zweck: The C4 Viewpoint specifies Standard Operational Activities that can be re-used across multiple logical architectures (e.g. in L4, Logical Activities).

**C4-Maps To Capability**

_Elemente:_
- **Capability** (`Class`) – A high level specification of the enterprise's ability to execute a specified course of action.
- **StandardOperationalActivity** (`Activity`) – A sub-type of OperationalActivity that is a standard operating procedure.

_Beziehungen:_
- **MapsToCapability** (`Abstraction`) – A tuple denoting that an Activity contributes to providing a Capability.

**C4-EnduringTask**

_Elemente:_
- **ActualEnduringTask** (`Object`) – An actual undertaking recognized by an enterprise as being essential to achieving its goals - i.e. a strategic specification of what the enterprise does.
- **EnduringTask** (`Class`) – A type of template behavior recognized by an enterprise as being essential to achieving its goals - i.e. a template for a strategic specification of what the enterprise does.

_Beziehungen:_
- **CapabilityForTask** (`Abstraction`) – A tuple that asserts that a Capability is required in order for an Enterprise to conduct a phase of an EnduringTask.

**Strategic Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

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

## C5 – C5 - Effects

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-C5-Toolbox`
- Zweck: The purpose of the C5 Viewpoint is to describe the operational effect of the capabilities, activities and services according to the expected goals. The C5 Viewpoint is high-level description that should be easily understood by non-technical readers.

**C5-Desirer**

_Elemente:_
- **Capability** (`Class`) – A high level specification of the enterprise's ability to execute a specified course of action.

**C5-Actual State**

_Elemente:_
- **ActualCondition** (`Object`) – An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed.
- **ActualEnduringTask** (`Object`) – An actual undertaking recognized by an enterprise as being essential to achieving its goals - i.e. a strategic specification of what the enterprise does.
- **ActualEnterprisePhase** (`Object`) – The ActualState that describes the phase of an Enterprise endeavor.
- **ActualMeasurementSet** (`Object`) – A set of ActualMeasurements.
- **ActualProjectMilestone** (`Object`) – An event with a start date in a ActualProject from which progress is measured.
- **ActualPropertySet** (`Object`) – A set or collection of Actual properties.
- **ActualResource** (`Object`) – Role in an Organisation, where the role carries the authority to undertake a function - through the ActualOrganizationalResource given the role has the responsibility.

**C5-Relationships**

_Elemente:_
- **Environment** (`Class`) – A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using EnvironmentKind.

_Beziehungen:_
- **AchievedEffect** (`Dependency`) – A tuple that exists between an ActualState (e.g., observed/measured during testing) of an element that attempts to achieve a DesiredEffect and an Achiever.
- **DesiredEffect** (`Dependency`) – A tuple relating the Desirer (a Capability or OrganizationalResource) to an ActualState.
- **EnvironmentalCondition** (`Dependency`) – Relationship that indicates under which environment an exhibits-relationship takes place.
- **Exhibits** (`Abstraction`) – A tuple that exists between a CapableElement and a Capability that it meets under specific environmental conditions.
- **RealizedDesiredEffect** (`Dependency`) – Relationship that expresses which connector DesiredEffect the connector AchievedEffect realizes.
- **RealizingAchievedEffect** (`Dependency`) – Relationship that expresses which connector AchievedEffect realizes the connector DesiredEffect.

**Strategic Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

**C5-Achiever**

_Elemente:_
- **ActualOrganization** (`Object`) – An actual formal or informal organizational unit, e.g. "Driving and Vehicle Licensing Agency", "UAF team Alpha".
- **ActualPerson** (`Object`) – An individual human being.
- **ActualPost** (`Object`) – An actual, specific post, an instance of a Post "type" - e.g., "President of the United States of America." where the Post would be president.
- **ActualResource** (`Object`) – Role in an Organisation, where the role carries the authority to undertake a function - through the ActualOrganizationalResource given the role has the responsibility.
- **FieldedCapability** (`Object`) – An individual, fully-realized capability.

**C5-Achiever Types**

_Elemente:_
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **Organization** (`Class`) – A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose.
- **Person** (`Class`) – A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, nationality, etc).
- **Post** (`Class`) – A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).
- **ServiceSpecification** (`Class`) – The specification of a set of functionality provided one element for the use of others.
- **StandardOperationalActivity** (`Activity`) – A sub-type of OperationalActivity that is a standard operating procedure.

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

## C7 – C7 - Performance Parameters

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-C7-Toolbox`
- Zweck: In the C7 Viewpoint the capability requirements (and existing capabilities) can be expressed in terms of Measures of Effectiveness (MoEs). These are high-level metrics used to judge the level of capability.

**C7-Measurements**

_Elemente:_
- **ActualCondition** (`Object`) – An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed.
- **ActualEnvironment** (`Object`) – The ActualState that describes the circumstances of an Environment.
- **ActualLocation** (`Object`) – The ActualState that describes a physical location, for example using text to provide an address, Geo-coordinates, etc.
- **Capability** (`Class`) – A high level specification of the enterprise's ability to execute a specified course of action.
- **Measurement** (`Part`) – A property of an element representing something in the physical world, expressed in amounts of a unit of measure.
- **MeasurementType** (`Class`) – A type of a property representing something in the physical world, expressed in amounts of a unit of measure.

_Beziehungen:_
- **EnvironmentalContext** (`Dependency`) – Relationship that indicates under which condition an measurement counts.
- **OwnsMeasurement** (`Dependency`) – A relationship that expresses which measurement or measurement type an element owns.

**Strategic Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

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

## C8 – C8 - Planning Assumptions

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-C8-Toolbox`
- Zweck: The C8 Viewpoint is concerned with identification and description of assumptions that have been made for the implementation of capabilities. Assumptions can be expressed by means of requirements.

**Strategic Constraints**

_Elemente:_
- **Classification** (`Class`) – Classification according to STANAG 1059.
- **DocumentReference** (`Class`) – The element describes a regulation, instruction or a general document.
- **Reference** (`Class`) – Element describes all types of references.
- **SMEReference** (`Class`) – Element stands for a result of a workshop or expert knowledge.
- **StrategicConstraint** (`Class`) – A Rule governing a capability.

_Beziehungen:_
- **Classified** (`Dependency`) – Relationship that indicates which classification an element has.
- **JustifiedBy** (`Dependency`) – Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference).
- **OriginatesFrom** (`Dependency`) – Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference).
- **Satisfy** (`Dependency`) – This relation states that an constraint affects an element.

**Implements Constraints**

_Elemente:_
- **OperationalConstraint** (`Class`) – A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc.
- **ResourceConstraint** (`Class`) – A rule governing the structural or functional aspects of an implementation.
- **ServicePolicy** (`Class`) – A constraint governing the use of one or more ServiceSpecifications.

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

## Cr – Cr - Capability Roadmap

- Diagrammtyp: `Diagram_Custom`
- Toolbox: `NAFv4-ADMBw-Cr-Toolbox`
- Zweck: The Cr Viewpont supports the Capability Audit process by providing a method to identify gaps or duplications in capability provision. Cr indicates capability increments, which are derived from delivery milestones within acquisition projects.

**Cr-Capability && Configuration**

_Elemente:_
- **Capability** (`Class`) – A high level specification of the enterprise's ability to execute a specified course of action.
- **CapabilityConfiguration** (`Class`) – A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability).
- **Environment** (`Class`) – A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using EnvironmentKind.
- **FieldedCapability** (`Object`) – An individual, fully-realized capability.

_Beziehungen:_
- **EnvironmentalCondition** (`Dependency`) – Relationship that indicates under which environment an exhibits-relationship takes place.
- **Exhibits** (`Abstraction`) – A tuple that exists between a CapableElement and a Capability that it meets under specific environmental conditions.

**Cr-Project**

_Elemente:_
- **ActualProject** (`Object`) – A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs.
- **ActualProjectMilestone** (`Object`) – An event with a start date in a ActualProject from which progress is measured.
- **Project** (`Class`) – A type that describes types of time-limited endeavours that are required to meet one or more Capability needs.
- **ProjectMilestone** (`Class`) – A type of event in a Project by which progress is measured.
- **ProjectMilestoneRole** (`Part`) – The role played by a ProjectMilestone in the context of a Project.

_Beziehungen:_
- **ActualProjectDependency** (`Dependency`) – Relationship that is a dependency of a actualproject on a actualproject.
- **ActualResourceNeededByActualProjectMilestone** (`Dependency`) – A relationship that expresses that an actual resource is needed by actual project milestones.
- **ActualResourceToActualProjectMilestone** (`Dependency`) – A relationship that expresses that an actual resource is mapped to actual project milestones.
- **MilestoneDependency** (`Dependency`) – A tuple between two ActualProjectMilestones that denotes one ActualProjectMilestone follows from another.
- **OwnedMilestone** (`Dependency`) – Relationship that expresses that actual project has a actual milestone.
- **ProjectMilestoneToProjectTheme** (`Dependency`) – A relationship that expresses which project theme is handled by which project milestone.
- **ProjectSequence** (`Dependency`) – A tuple between two ActualProjects that denotes one ActualProject cannot start before the previous ActualProject is finished.
- **RequiredResource** (`Dependency`) – Relationship that indicates which resources a project milestone requires
- **VersionReleased** (`Dependency`) – A relationship that expresses that an actual project milestone releases an versioned element.
- **VersionWithdrawn** (`Dependency`) – A relationship that expresses that an actual project milestone withdraws an versioned element.

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