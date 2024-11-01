# calculator/plugin_loader.py
import importlib
import os

class PluginLoader:
    def load_plugins(self):
        plugins = {}
        plugin_folder = os.path.join(os.path.dirname(__file__), "plugins")

        for file_name in os.listdir(plugin_folder):
            if file_name.endswith(".py") and file_name != "__init__.py":
                module_name = file_name[:-3]
                module = importlib.import_module(f"calculator.plugins.{module_name}")
                plugin = getattr(module, 'plugin', None)
                if plugin:
                    plugins[module_name] = plugin
        return plugins

