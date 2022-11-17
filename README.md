# Lab 4. Introduction to Local Search

## TODO:

Fill missing code according to the `TODO:` comments in the following files (listed in the recommended order):

- [ ] `local_search/algorithms/hill_climbing/random_choice_hill_climbing.py`
- [ ] `local_search/algorithms/hill_climbing/best_choice_hill_climbing.py`
- [ ] `local_search/algorithms/hill_climbing/worst_choice_hill_climbing.py`
- [ ] `local_search/algorithms/simulated_annealing.py`
- [ ] `local_search/problems/graph_coloring_problem/moves/kempe_chain.py`
- [ ] `local_search/problems/graph_coloring_problem/goals/goal.py`

## Grading

* [ ] Make sure, you have a **private** group
  * [how to create a group](https://docs.gitlab.com/ee/user/group/#create-a-group)
* [ ] Fork this project into your private group
  * [how to create a fork](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html#creating-a-fork)
* [ ] Add @bobot-is-a-bot as the new project's member (role: **maintainer**)
  * [how to add an user](https://docs.gitlab.com/ee/user/project/members/index.html#add-a-user)

## How To Submit Solutions

* [ ] Clone repository: git clone:
    ```bash
    git clone <repository url>
    ```
* [ ] Solve the exercises
    * use MiniZincIDE, whatever
* [ ] Commit your changes
    ```bash
    git add <path to the changed files>
    git commit -m <commit message>
    ```
* [ ] Push changes to the gitlab master branch
    ```bash
    git push -u origin master
    ```

The rest will be taken care of automatically. You can check the `GRADE.md` file for your grade / test results. 
Be aware that it may take some time (up to one hour) till this file

## How To Run

```bash
pip install -e .
python run.py solve -c [PATH_TO_CONFIG]
```

There are several config examples in the project directory, the `la_config.json` is quite cool, because it show how one can generate avatars with local search :)

If a required option is not specified in the config file (or the config file is not specified at all), the CLI will ask you for the missing values in an interactive manner. 

### CLI 

Course provides you with a command line interface, to facilitate developing and debugging of algorithms.
You can check commands by running:

```bash
python run.py --help
```

If you are interested in how some concrete command works you can check it by running:

```bash
python run.py COMMAND_NAME --help
```
