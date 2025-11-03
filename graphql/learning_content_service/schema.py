import collections
import sys

if sys.version_info >= (3, 11):
    import collections.abc
    collections.Mapping = collections.abc.Mapping
    collections.Iterable = collections.abc.Iterable
    
import graphene

class LearningModule(graphene.ObjectType):
    module_id = graphene.String()
    topic = graphene.String()
    difficulty = graphene.String()
    learning_style = graphene.String()
    prerequisite = graphene.String()

class Query(graphene.ObjectType):
    modules = graphene.List(LearningModule)

    def resolve_modules(root, info):
        # Hardcoded data for demonstration, simulating a database call
        return [
            LearningModule(module_id="M001", topic="Algebra Basics", difficulty="Easy", learning_style="Visual", prerequisite="None"),
            LearningModule(module_id="M002", topic="Geometry Intro", difficulty="Easy", learning_style="Auditory", prerequisite="None"),
            LearningModule(module_id="M003", topic="Functions", difficulty="Medium", learning_style="Visual", prerequisite="M001"),
            LearningModule(module_id="M004", topic="Calculus Intro", difficulty="Hard", learning_style="Visual", prerequisite="M003"),
            LearningModule(module_id="M005", topic="Advanced Physics", difficulty="Hard", learning_style="Kinesthetic", prerequisite="M004"),
            LearningModule(module_id="M006", topic="Basic Chemistry", difficulty="Medium", learning_style="Visual", prerequisite="None"),
        ]

schema = graphene.Schema(query=Query)