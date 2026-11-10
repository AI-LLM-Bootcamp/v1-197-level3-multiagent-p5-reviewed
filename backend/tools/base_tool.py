# Original version: the app imported BaseTool and SerperDevTool from the
# crewai-tools package. That version of crewai-tools needs lancedb 0.5.x,
# and those lancedb versions are no longer available on PyPI, so the
# project could not be installed anymore. This app only used these two
# small pieces of crewai-tools, so they now live in the tools folder.
#
# This version of CrewAI works with LangChain tools, so our BaseTool is a
# LangChain tool. Like the one in crewai-tools, it shows the agent the
# tool's name, arguments and description in a single line, for example:
# Search the internet(search_query: 'string') - A tool that ...
from langchain_core.tools import BaseTool as LangChainBaseTool


class BaseTool(LangChainBaseTool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        args = [
            f"{arg}: '{attribute['type']}'"
            for arg, attribute in self.args_schema.schema()["properties"].items()
        ]
        description = self.description.replace("\n", " ")
        self.description = f"{self.name}({', '.join(args)}) - {description}"
