import time
import click
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def create_repo(name, un, pd, option, readme, des):
    browser = webdriver.Chrome()
    browser.get("https://www.github.com/login")
    sleep(3)
    try:
        username = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.ID, "login_field")))
        username.clear()
        username.send_keys(un)
        passwd = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.ID, "password")))
        passwd.clear()
        passwd.send_keys(pd)
        login_btn = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.NAME, "commit")))
        login_btn.click()
        browser.get("https://www.github.com/new")
        repo_name = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.ID, "repository_name")))
        repo_name.clear()
        repo_name.send_keys(name)
        description = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.ID, "repository_description")))
        description.clear()
        description.send_keys(des)
        if option == "pub":
            pub_tog = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "repository_visibility_public")))
            pub_tog.click()
        elif option == "pri":
            pri_tog = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "repository_visibility_private")))
            pri_tog.click()
            sleep(2)
        else:
            pub_tog = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "repository_visibility_public")))
            pub_tog.click()
            click.echo(f"Bad command {option}, the repo is taken to be public")
        if readme == "y":
            read_me = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "repository_auto_init")))
            read_me.click()
        elif readme == "n":
            click.echo("Didn't add a Read me file to your repo as you told")
        else:
            click.echo(f"Bad command {readme}, could not add a readme file")
        done_btn = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="new_repository"]/div[4]/button')))
        done_btn.click()
        # /html/body/div[1]/header/div[7]/details/summary
        drop_down = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
        drop_down.click()
        sleep(1)
        sign_out = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
        sign_out.click()
        sleep(1)
        browser.quit()
        command(repon=name, un=un)
        click.secho(
            f"Successfully created {name} at https://github.com/{un}/{name}", fg='blue')
        click.secho(
            f"If you want to clone the repo then type git clone https://github.com/{un}/{name}.git in your desired directory", fg='green')
    except:
        browser.quit()


def delete_repo(name, un, pd, confirm, option):
    if confirm == "y":
        if (option == "pub" or option == "pri"):
            browser = webdriver.Chrome()
            browser.get("https://www.github.com/login")
            sleep(2)
            try:
                username = WebDriverWait(browser, 6).until(
                    EC.presence_of_element_located((By.ID, "login_field")))
                username.clear()
                username.send_keys(un)
                passwd = WebDriverWait(browser, 6).until(
                    EC.presence_of_element_located((By.ID, "password")))
                passwd.clear()
                passwd.send_keys(pd)
                login_btn = WebDriverWait(browser, 6).until(
                    EC.presence_of_element_located((By.NAME, "commit")))
                login_btn.click()
                browser.get(f"https://www.github.com/{un}/{name}/settings")
                if option == "pri":
                    delete = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                        # //*[@id="options_bucket"]/div[10]/ul/li[4]/details/summary
                        (By.XPATH, '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')))
                    delete.click()
                elif option == "pub":
                    delete = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                        # //*[@id="options_bucket"]/div[10]/ul/li[4]/details/summary
                        (By.XPATH, '//*[@id="options_bucket"]/div[10]/ul/li[4]/details/summary')))
                    delete.click()
                else:
                    click.echo(
                        f"Bad command {option}, couldn't delete the repo")
                if option == "pub":
                    delete_name = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="options_bucket"]/div[10]/ul/li[4]/details/details-dialog/div[3]/form/p/input')))
                    delete_name.clear()
                    delete_name.send_keys(f"{un}/{name}")
                elif option == "pri":
                    delete_name = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')))
                    delete_name.clear()
                    delete_name.send_keys(f"{un}/{name}")
                else:
                    click.echo(
                        f"Bad command {option}, couldn't delete the repo")
                if option == "pub":
                    confirm_btn_main = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="options_bucket"]/div[10]/ul/li[4]/details/details-dialog/div[3]/form/button')))
                    confirm_btn_main.click()
                elif option == "pri":
                    confirm_btn_main = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')))
                    confirm_btn_main.click()
                else:
                    click.echo(
                        f"Bad command {option}, couldn't delete the repo")
                drop_down = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
                drop_down.click()
                sleep(2)
                sign_out = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
                sign_out.click()
                sleep(2)
                click.secho(
                    f"Successfully deleted {name} at https://github.com/{un}/{name}", fg='green')
            except:
                browser.quit()
                click.secho(
                    f"Could not delete the repo at https://github.com/{un}/{name}", fg='red')

        else:
            click.echo(f"Bad command {option}, failed deleteing the repo")
    elif confirm == "n":
        click.echo(f"Aborted the deletion of {name} repo")
    else:
        click.echo(f"Bad command {confirm}, couldn't delete the repo")


def ListRepos(uname, pwd):
    browser = webdriver.Chrome()
    browser.get(f"https://github.com/login")
    sleep(3)
    try:
        username = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.ID, "login_field")))
        username.clear()
        username.send_keys(uname)
        passwd = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.ID, "password")))
        passwd.clear()
        passwd.send_keys(pwd)
        login_btn = WebDriverWait(browser, 6).until(
            EC.presence_of_element_located((By.NAME, "commit")))
        login_btn.click()
        browser.get(f"https://github.com/{uname}?tab=repositories")
        repo = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "user-repositories-list")))
        nameList = repo.find_elements_by_tag_name('li')
        print('---------------------------------')
        for name in nameList:
            title = name.find_element_by_class_name("wb-break-all")
            print(title.text)
        drop_down = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
        drop_down.click()
        sleep(2)
        sign_out = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
        sign_out.click()
        sleep(2)
    except:
        browser.quit()


def themeSet(uname, pwd, theme_name):
    try:
        if theme_name == "light":
            browser = webdriver.Chrome()
            browser.get(f"https://github.com/login")
            sleep(3)
            username = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "login_field")))
            username.clear()
            username.send_keys(uname)
            passwd = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "password")))
            passwd.clear()
            passwd.send_keys(pwd)
            login_btn = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.NAME, "commit")))
            login_btn.click()
            browser.get(f"https://github.com/settings/appearance")
            light_theme = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "option-light")))
            light_theme.click()
            drop_down = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
            drop_down.click()
            sleep(2)
            sign_out = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
            sign_out.click()
            sleep(2)
            click.echo(
                f"Successfully Updated your GitHub Theme to {theme_name} theme")
        elif theme_name == "dark":
            browser = webdriver.Chrome()
            browser.get(f"https://github.com/login")
            sleep(3)
            username = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "login_field")))
            username.clear()
            username.send_keys(uname)
            passwd = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "password")))
            passwd.clear()
            passwd.send_keys(pwd)
            login_btn = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.NAME, "commit")))
            login_btn.click()
            browser.get(f"https://github.com/settings/appearance")
            dark_theme = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "option-dark")))
            dark_theme.click()
            drop_down = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
            drop_down.click()
            sleep(2)
            sign_out = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
            sign_out.click()
            sleep(2)
            click.echo(
                f"Successfully Updated your GitHub Theme to {theme_name} theme")
        elif theme_name == "default":
            browser = webdriver.Chrome()
            browser.get(f"https://github.com/login")
            sleep(3)
            username = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "login_field")))
            username.clear()
            username.send_keys(uname)
            passwd = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "password")))
            passwd.clear()
            passwd.send_keys(pwd)
            login_btn = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.NAME, "commit")))
            login_btn.click()
            browser.get(f"https://github.com/settings/appearance")
            def_theme = WebDriverWait(browser, 6).until(
                EC.presence_of_element_located((By.ID, "option-auto")))
            def_theme.click()
            drop_down = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
            drop_down.click()
            sleep(2)
            sign_out = WebDriverWait(browser, 6).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
            sign_out.click()
            sleep(2)
            click.echo(
                f"Successfully Updated your GitHub Theme to {theme_name} theme")
        else:
            click.echo("No Such theme found for Github")
    except:
        browser = webdriver.Chrome()
        browser.quit()


def command(repon, un):
    # os.system('dir')
    # click.echo('')
    # path = os.system('pwd')
    # click.echo(path)
    path = os.getcwd()
    click.secho('GIT PROCCESS', bold=True, fg="bright_yellow")
    option = click.prompt(
        f'Do you want to initialize git here "{path}" [y/n/man]')
    if option == 'y':
        os.system('git init')
        os.system(f'echo "# {repon}" >> README.md')
        os.system('git add .')
        msg = click.prompt('Please enter the commit message')
        os.system(f'git commit -m "{msg}"')
        branch = click.prompt(
            "Please enter the branch name to which you wanna commit these files")
        os.system(f'git branch -M {branch}')
        os.system(
            f'git remote add origin https://github.com/{un}/{repon}.git')
        os.system(f'git push -uf origin {branch}')
    elif option == 'n':
        click.secho('Didnt initialize, script terminated', fg='red')
        sys.exit()
    elif option == 'man':
        name = click.prompt(click.style(
            'In which directory do you want to git', fg='green'))
        dirpath = os.path.isdir(name)
        if dirpath is True:
            os.chdir(name)
            dir = os.getcwd()
            click.echo(f'Changed directory to: {dir}')
            os.system('git init')
            os.system(f'echo "# {repon}" >> README.md')
            os.system('git add .')
            msg = click.prompt('Please enter the commit message')
            os.system(f'git commit -m "{msg}"')
            branch = click.prompt(
                "Please enter the branch name to which you wanna commit these files")
            os.system(f'git branch -M {branch}')
            os.system(
                f'git remote add origin https://github.com/{un}/{repon}.git')
            os.system(f'git push -uf origin {branch}')
        else:
            click.echo(f'Sorry, Directory {name} doesnt exist')
    else:
        click.echo(f'Wrong choice {option}')


def send_commands():
    # os.system('dir')
    # click.echo('')
    # path = os.system('pwd')
    # click.echo(path)
    path = os.getcwd()
    click.secho('GIT PROCCESS', bold=True, fg="bright_yellow")
    option = click.prompt(
        f'Is this the path to the repo files "{path}" [y/n]')
    if option == 'y':
        git_dir = os.path.isdir(".git")
        if git_dir is True:
            os.system('git add .')
            msg = click.prompt('Please enter the commit message')
            os.system(f'git commit -m "{msg}"')
            branch = click.prompt(
                "Please enter the branch name to which you wanna commit these files")
            os.system(f'git branch -M {branch}')
            os.system(f'git push -uf origin {branch}')
        else:
            click.echo("No .git folder folder found in this path.")
            click.echo(f"Initialising git directory here in this path: {path}")
            os.system("git init")
            os.system('git add .')
            msg = click.prompt('Please enter the commit message')
            os.system(f'git commit -m "{msg}"')
            branch = click.prompt(
                "Please enter the branch name to which you wanna commit these files")
            os.system(f'git branch -M {branch}')
            os.system(f'git push -uf origin {branch}')

    elif option == 'n':
        name = click.prompt(click.style(
            'Enter the directory path where git is initialized and the project files are present', fg='green'))
        dirpath = os.path.isdir(name)
        if dirpath is True:
            os.chdir(name)
            dir = os.getcwd()
            click.echo(f'Changed directory to: {dir}')
            os.system("git init")
            os.system('git add .')
            msg = click.prompt('Please enter the commit message')
            os.system(f'git commit -m "{msg}"')
            branch = click.prompt(
                "Please enter the branch name to which you wanna commit these files")
            os.system(f'git branch -M {branch}')
            os.system(f'git push -uf origin {branch}')
        else:
            click.echo(f'Sorry, Directory {name} doesnt exist')
    else:
        click.echo(f'Wrong choice {option}')


@click.group()
def cli():
    pass


@click.command(help="Creates Repo to Github")
@click.argument("name", type=str)
@click.option('-u', "--un", required=True, prompt="Username", help="GitHub username")
@click.option('-p', "--pd", required=True, hide_input=True, prompt="Password", help="Github Password")
@click.option('-d', "--des", prompt="A sweet description of your repo", help="Adds Description to the repo")
@click.option('-s', "--private", prompt="The repo is private or public[pri/pub]", help="Repo is Private or Public")
@click.option('-r', "--readme", prompt="Do you add a Readme file to your repo[y/n]", help="Addition of a readme file to the repo")
@click.pass_context
def create(ctx, name, un, pd, des, private, readme):
    """
    Creates GitHub Repositories
    """
    ctx.invoke(create_repo, name=name, un=un, pd=pd,
               des=des, option=private, readme=readme)


@click.command(help="Deletes the Repo from Github")
@click.argument("name", type=str)
@click.option('-u', "--un", required=True, prompt="Username", help="GitHub username")
@click.option('-p', "--pd", required=True, hide_input=True, prompt="Password", help="Github Password")
@click.option('-c', "--confirm", prompt="Are you sure that you want to delete this repo[y/n]", help="Confirmation to delete the repo")
@click.option('-o', "--option", prompt="Is it a private or public repo[pub/pri]")
@click.pass_context
def delete(ctx, name, option, un, pd, confirm):
    """
    Deletes GitHub Repositories
    """
    ctx.invoke(delete_repo, option=option, name=name,
               un=un, pd=pd, confirm=confirm)


@click.command(help="Lists the Repos of your Account")
@click.option('-u', "--user", required=True, prompt="Username", help="GitHub username")
@click.option('-p', "--pd", required=True, hide_input=True, prompt="Password", help="Github Password")
@click.pass_context
def list(ctx, user, pd):
    """
    Lists the Repos of the Account
    """
    ctx.invoke(ListRepos, uname=user, pwd=pd)


@click.command(help="Changes your GitHub Account theme")
@click.option('-u', "--user", required=True, prompt="Username", help="GitHub username")
@click.option('-p', "--pd", required=True, hide_input=True, prompt="Password", help="Github Password")
@click.option('-n', "--name", required=True, prompt="Which theme[light, dark, default] would you like to set", help="Github Theme")
@click.pass_context
def theme(ctx, user, pd, name):
    """
    Changes the Github Theme
    """
    ctx.invoke(themeSet, uname=user, pwd=pd, theme_name=name)


@click.command(help="Run Commands")
@click.pass_context
def ga(ctx):
    """
    Run all git commands to add, commit and push
    """
    ctx.invoke(send_commands)


cli.add_command(create)
cli.add_command(delete)
cli.add_command(list)
cli.add_command(theme)
cli.add_command(ga)
