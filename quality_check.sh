#!/usr/bin/env bash
# Perform quality checks of the card_deck library.

run_install_check() {
  # Install card_deck library
  echo "Installing card_deck"
  python3 -m pip install git+https://github.com/theStygianArchitect/card_deck.git@main
  exit_code=$?

  if [ ${exit_code} != 0 ]; then
    exit ${exit_code}
  fi
}

run_uninstall_check() {
  # Uninstall card_deck library
  echo "Uninstalling card_deck"
  python3 -m pip uninstall -y card_deck
  exit_code=$?

  if [ ${exit_code} != 0 ]; then
    exit ${exit_code}
  fi
}

run_automated_docs() {
  # Rebuilding documentation
  echo "Rebuilding documentation"
  cd ./doc_src && make github
}

run_bandit_check() {
  # bandit scan
  echo "Starting bandit check"
  for python_file_name in "${app_directory_list[@]}"; do
    echo "  ${python_file_name}"
    uv run bandit -c pyproject.toml -r -q "${python_file_name}"
    exit_code=$?

    if [ ${exit_code} != 0 ]; then
      exit ${exit_code}
    fi
  done
  echo "Passed bandit check."
}

run_mypy_check() {
  # code type linting
  echo "Starting mypy check"
  for python_file_name in "${app_directory_list[@]}"; do
    echo "  ${python_file_name}"
    uv run mypy "${python_file_name}"
    exit_code=$?

    if [ ${exit_code} != 0 ]; then
      exit ${exit_code}
    fi
  done
  echo "Passed mypy check."
}

run_pycodestyle_check() {
  # pycodestyle scan
  echo "Starting pycodestyle check"
  for python_file_name in "${app_directory_list[@]}"; do
    echo "  ${python_file_name}"
    uv run pycodestyle --max-line-length 120 "${python_file_name}"
    exit_code=$?

    if [ ${exit_code} != 0 ]; then
      exit ${exit_code}
    fi
  done
  echo "Passed pycodestyle check."
}

run_pydocstyle_check() {
  # pydocstyle scan
  echo "Starting pydocstyle check"
  for python_file_name in "${app_directory_list[@]}"; do
    echo "  ${python_file_name}"
    uv run pydocstyle "${python_file_name}"
    exit_code=$?

    if [ ${exit_code} != 0 ]; then
      exit ${exit_code}
    fi
  done
  echo "Passed pydocstyle check."
}

run_pylint_check() {
  # code linting
  echo "Starting pylint check"
  for python_file_name in "${app_directory_list[@]}"; do
    echo "  ${python_file_name}"
    uv run pylint -s no "${python_file_name}"
    exit_code=$?

    if [ ${exit_code} != 0 ]; then
      exit ${exit_code}
    fi
  done
  echo "Passed pylint check."
}

run_ruff_check() {
  # code linting
  echo "Starting ruff check"
  for python_file_name in "${app_directory_list[@]}"; do
    echo "  ${python_file_name}"
    uv run ruff check --quiet "${python_file_name}"
    exit_code=$?

    if [ ${exit_code} != 0 ]; then
      exit ${exit_code}
    fi
  done
  echo "Passed ruff check."
}

run_pytest() {
  # Unit Testing
  echo "Starting project tests"
  uv run python -m pytest -x "${test_directory}"
  exit_code=$?

  if [ ${exit_code} != 0 ]; then
    exit ${exit_code}
  fi
  echo "Passed project tests."
}

run_coverage() {
  # Unit Testing
  echo "Starting project coverage tests"
  uv run coverage run -m pytest "${test_directory}"
  exit_code=$?

  if [ ${exit_code} != 0 ]; then
    exit ${exit_code}
  fi

  echo "Generating coverage report"
  uv run coverage report -m
  exit_code=$?
  echo "Coverage report generated."
}

run_dependency_check() {
  # security code scanning
  echo "Starting pip audit"
  uv run pip-audit
  exit_code=$?

  if [ ${exit_code} != 0 ]; then
    exit ${exit_code}
  fi
  echo "Passed pip audit."
}

run_update_all_the_things() {
  # Update All the Things
  echo "Updating ALL TEH Things!!!!1!"

  echo "Updating project requirements!"
  echo "There are none right now"
  echo "whomp whomp"
  sleep 3

  echo "Updating security packages!"
  uv remove --group security bandit pip-audit
  uv add --group security bandit pip-audit

  echo "Updating linting packages!"
  uv remove --group linting mypy pycodestyle pydocstyle pylint ruff
  uv add --group linting mypy pycodestyle pydocstyle pylint ruff

  echo "Updating testing packages!"
  uv remove --group testing pytest pytest-cov pytest-xdist
  uv add --group testing pytest pytest-cov pytest-xdist

  echo "Updating documentation packages!"
  uv remove --group docs myst-parser sphinx sphinx-autodoc-typehints sphinx-immaterial
  uv add --group docs myst-parser sphinx sphinx-autodoc-typehints sphinx-immaterial

  echo "All TEH Things updated!!!!1!"
}

run_security_check() {
  # run all security checks
  echo "Running all security checks"
  run_bandit_check
  run_dependency_check
}

run_linting_check() {
  # run all linting checks
  echo "Running all linting checks"
  run_ruff_check
  run_pylint_check
  run_pycodestyle_check
  run_pydocstyle_check
  run_mypy_check
}

quality_check() {
  # run all checks
  echo "Running all quality checks"
  run_dependency_check
  run_bandit_check
  run_ruff_check
  run_pylint_check
  run_pydocstyle_check
  run_mypy_check
  run_coverage
  run_automated_docs
}

verify_card_deck_installation() {
  # verify installation
  echo "Verifying card_deck installation"
  run_uninstall_check
  run_install_check
}

show_usage() {
  # Display usage
  echo "Card Deck Quality Check Manual"
  echo "USAGE"
  echo "  quality_check [-a] [-d] [-l] [-q [<check type>]] [-s] [-t]"
  echo ""
  echo "OPTIONS"
  echo "  -a  Run all quality checks. (DEFAULT)"
  echo "  -c  Run coverage report."
  echo "  -d  Build documentation."
  echo "  -h  Shows Usage."
  echo "  -i  Verify card_deck installation."
  echo "  -l  Run linting checks."
  echo "  -s  Run security checks."
  echo "  -t  Run project's tests."
  echo "  -u  Upgrade package requirements in the pyproject.toml file."
  echo "  -q  Run specific quality check."
  echo "    bandit         Static analysis checking with bandit."
  echo "    coverage       Run Coverage report for project."
  echo "    documentation  Automatically build documentation using Sphinx."
  echo "    installation   Validate the installation of card_deck."
  echo "    mypy           Pep484 type hinting with mypy."
  echo "    pip-audit      Dependency vulnerability checking with pip-audit"
  echo "    pycodestyle    Pep008 checking with pycodestyle"
  echo "    pydocstyle     Pep257 checking with pydocstyle"
  echo "    pylint         Code linting with pylint"
  echo "    pytest         Run project's tests"
  echo "    ruff           Code linting with ruff"
  echo
}

# declare vars
app_directory_list=(
  card_deck/*.py
  tests/*.py
)
test_directory="tests"
read -r -d '' options << EOM
Please use [bandit | coverage | documentation | installation | mypy | pip-audit |
            pycodestyle | pydocstyle | pylint | pytest | ruff]
EOM

while getopts 'aclhistduq:' flag; do
  case "${flag}" in
    a) quality_check ;;
    c) run_coverage ;;
    s) run_security_check ;;
    h) show_usage ;;
    i) verify_card_deck_installation ;;
    l) run_linting_check ;;
    t) run_pytest ;;
    d) run_automated_docs ;;
    u) run_update_all_the_things ;;
    q) case "${OPTARG}" in
      bandit) run_bandit_check ;;
      coverage) run_coverage ;;
      documentation) run_automated_docs ;;
      installation) verify_card_deck_installation ;;
      mypy) run_mypy_check ;;
      pip-audit) run_dependency_check ;;
      pycodestyle) run_pycodestyle_check ;;
      pydocstyle) run_pydocstyle_check ;;
      pylint) run_pylint_check ;;
      pytest) run_pytest ;;
      ruff) run_ruff_check ;;
      update) run_update_all_the_things ;;
      *)
        echo "${OPTARG} is a bad option!!"
        echo "${options}"
        exit 1
        ;;
    esac ;;
    *) show_usage ;;
  esac
done
