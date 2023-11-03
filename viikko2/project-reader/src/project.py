class Project:
    def __init__(self, name, description, app_license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.app_license = app_license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        #return ", ".join(dependencies) if len(dependencies) > 0 else "-"
        if len(dependencies) > 0:
            result = "\n"
            result += "\n".join(["- " + dep for dep in dependencies])
        else:
            result = "\n-"

        return result 

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.app_license}\n"
            f"\nAuthors: {self._stringify_dependencies(self.authors)}\n"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
