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
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"os":"linux","editor":{"mode":"extension","agent":"vscode","version":"5.0.71"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"https://zany-space-fishstick-g74px9ppvq52vv9j-3000.app.github.dev","contact":"https://github.com/learnpack/learnpack/issues/new","language":"python3","autoPlay":true,"projectType":"tutorial","grading":"isolated","exercisesPath":"./exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":[],"actions":[],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"suggestions":{"agent":"vscode"},"warnings":{"agent":null},"slug":"python-modules-tutorial","title":{"en":"Learn Python Modules","es":"Aprender Módulos de Python"},"repository":"https://github.com/learnpack/python-modules","preview":"https://github.com/learnpack/python-modules/blob/master/preview.gif?raw=true","description":{"en":"Learn how to use and create Python modules, from basic imports to advanced concepts","es":"Aprende a usar y crear módulos de Python, desde importaciones básicas hasta conceptos avanzados"},"difficulty":"beginner","duration":6,"videoSolutions":false,"bugsLink":"https://github.com/learnpack/python-modules/issues/new","graded":true,"technologies":["python","modules"],"telemetry":{"batch":"https://breathecode.herokuapp.com/v1/assignment/me/telemetry"},"video":{"intro":{"es":"https://www.youtube.com/watch?v=IXNSwnN-YqM","en":"https://www.youtube.com/watch?v=amyDNhZwGJQ"}},"translations":[]}')])
