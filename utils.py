import os


class DirectoryHelper:

    @staticmethod
    def root_path(project_name: str = 'all_about_python') -> str:
        """get the current project root path
        Args:
            project_name (str, optional): project name
        Returns:
            str: project root path
        """
        project_name = 'all_about_python' if project_name is None else project_name
        project_path = os.path.abspath(os.path.dirname(__file__))
        root_path = project_path[
                    :project_path.find("{}".format(project_name)) + len("{}".format(project_name + os.sep))]
        return root_path

