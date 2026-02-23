# Domain-Driven Design: Conceptos Clave

## Domain
Área del negocio que el sistema busca resolver, incluyendo reglas, procesos y decisiones.

## Domain Model
Representación conceptual del dominio dentro del software, expresada en código.

## Ubiquitous Language
Lenguaje común entre negocio y desarrollo, usado en conversaciones, documentación y código.

## Model-Driven Design
El código es una expresión directa del modelo de dominio; no existe un modelo separado.

## Layered Architecture
Organización del sistema en capas para aislar la lógica del dominio de detalles técnicos.

- Presentation  
- Application  
- Domain  
- Infrastructure  

## Application Layer
Coordina casos de uso y delega la lógica de negocio al dominio.

## Domain Layer
Contiene el modelo de dominio, las reglas del negocio y su comportamiento.

## Infrastructure Layer
Implementa detalles técnicos como persistencia, mensajería y servicios externos.

## Entity
Objeto del dominio con identidad propia que se mantiene a lo largo del tiempo.

## Value Object
Objeto inmutable sin identidad, definido únicamente por sus atributos.

## Service
Operación del dominio que no pertenece naturalmente a una entidad u objeto de valor.

## Aggregate
Conjunto de objetos del dominio tratados como una unidad de consistencia.

## Aggregate Root
Entidad principal del agregado y único punto de acceso desde el exterior.

## Invariants
Reglas del negocio que deben cumplirse siempre dentro de un agregado.

## Factory
Encapsula la creación de objetos complejos garantizando su estado válido.

## Repository
Abstracción que permite acceder y persistir agregados sin exponer detalles técnicos.

## Specification
Regla de negocio encapsulada en un objeto evaluable y reutilizable.

## Supple Design
Diseño que prioriza claridad, expresividad y facilidad de cambio.

## Bounded Context
Límite explícito donde un modelo de dominio tiene significado consistente.

## Context Map
Describe las relaciones e integraciones entre distintos Bounded Contexts.

## Continuous Integration
Práctica para mantener el modelo consistente dentro de un mismo contexto.

## Shared Kernel
Parte del modelo compartida y mantenida por más de un equipo.

## Anti-Corruption Layer
Capa que protege el modelo propio de modelos externos incompatibles.

## Open Host Service
API estable expuesta para la integración con otros contextos.

## Published Language
Lenguaje común para el intercambio de información entre contextos.

## Conformist
Estrategia donde un contexto adopta el modelo de un proveedor externo.

## Separate Ways
Decisión de no integrar contextos y permitir su evolución independiente.
