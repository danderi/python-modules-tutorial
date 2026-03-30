import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")
def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
      if hasattr(metafunc,"config"):
          metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))
      elif hasattr(metafunc,"configuration"):
          metafunc.parametrize("stdin",metafunc.configuration.getoption('stdin'))
      else:
          raise Exception("Imposible to retrieve text configuration object")
    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
    if 'configuration' in metafunc.fixturenames:
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"os":"linux","editor":{"mode":"extension","agent":"vscode","version":"5.0"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"https://super-potato-6xwpv7v64px3rx6r-3000.app.github.dev","contact":"https://github.com/learnpack/learnpack/issues/new","language":"python3","autoPlay":true,"projectType":"tutorial","grading":"isolated","exercisesPath":"./exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":[],"actions":[],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"suggestions":{"agent":null},"warnings":{},"slug":"python-modules-tutorial","title":{"en":"Comprehensive to organize your code using Python modules","es":"Guía Completa de cómo organizar tu código usando módulos de python"},"repository":"https://github.com/learnpack/python-modules-tutorial","preview":"https://github.com/learnpack/python-modules-tutorial/blob/master/assets/preview.jpg?raw=true","description":{"en":"Learn how to use and create Python modules, from basic imports to advanced concepts. Students will learn how to organize their code efficiently and will be capable of creating reusable modules.","es":"Aprende a usar y crear módulos de Python, desde importaciones básicas hasta conceptos avanzados. Los estudiantes aprenderán a organizar su código de manera eficiente y serán capaces de crear módulos reutilizables."},"difficulty":"beginner","duration":6,"videoSolutions":false,"bugsLink":"https://github.com/learnpack/python-modules-tutorial/issues/new","graded":true,"technologies":["python","modules","code-organization","software-engineering","best-practices"],"telemetry":{"batch":"https://breathecode.herokuapp.com/v1/assignment/me/telemetry?asset_id=2180"},"translations":[]}')])
