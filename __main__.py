"""This is an example of how to annottate correctly the __main__.py
	
	Azkaban CLI: a lightweight command line interface for Azkaban.
Usage:
  azkaban build [-cp PROJECT] [-a ALIAS | -u URL | [-r] ZIP] [-o OPTION ...]
  azkaban info [-p PROJECT] [-f | -o OPTION ... | [-i] JOB ...]
  azkaban log [-a ALIAS | -u URL] EXECUTION [JOB]
  azkaban run [-jkp PROJECT] [-a ALIAS | -u URL] [-b | -m MODE] [-e EMAIL ...]
              [-o OPTION ...] FLOW [JOB ...]
  azkaban schedule [-jknp PROJECT] [-a ALIAS | -u URL] [-b | -m MODE]
                   [-e EMAIL ...] [-o OPTION ...]
                   (-d DATE -t TIME [-s SPAN] | -x CRON [-z TIMEZONE])
                   FLOW [JOB ...]
  azkaban upload [-cp PROJECT] [-a ALIAS | -u URL] ZIP
  azkaban -h | --help | -l | --log | -v | --version
Commmands:
  build*                        Build project and upload to Azkaban or save
                                locally the resulting archive.
  info*                         View information about jobs or files.
  log                           View workflow or job execution logs.
  run                           Run jobs or workflows. If no job is specified,
                                the entire workflow will be executed.
  schedule                      Schedule a workflow to be run either at a
                                specified date and time with optional recurring
                                time period, or based on a cron expression with
                                optional timezone.
  upload                        Upload archive to Azkaban server.
Arguments:
  EXECUTION                     Execution ID.
  JOB                           Job name.
  FLOW                          Workflow name. Recall that in the Azkaban world
                                this is simply a job without children.
  ZIP                           For `upload` command, the path to an existing
                                project zip archive. For `build`, the path
                                where the output archive will be built. If it
                                points to a directory, the archive will be
                                named after the project name (and version, if
                                present) and created in said directory.
Options:
  -a ALIAS --alias=ALIAS        Alias to saved URL and username. Will also try
                                to reuse session IDs for later connections.
  -b --bounce                   Skip execution if workflow is already running.
                                Shortcut for `--mode=skip`.
  -c --create                   Create the project if it does not exist.
  -d DATE --date=DATE           Date used for first run of a schedule. It must
                                be in the format `MM/DD/YYYY`.
  -e EMAIL --email=EMAIL        Email address to be notified when the workflow
                                finishes (can be specified multiple times).
  -f --files                    List project files instead of jobs. The first
                                column is the local path of the file, the
                                second the path of the file in the archive.
  -h --help                     Show this message and exit.
  -i --include-properties       Include project properties with job options.
  -j --jump                     Skip any specified jobs instead of only running
                                those.
  -k --kill                     Kill worfklow on first job failure.
  -l --log                      Show path to current log file and exit.
  -m MODE --mode=MODE           Concurrency mode. The default is to allow
                                concurrent executions. See also `--bounce`.
  -n --notify_early             Send any notification emails when the first job
                                fails rather than when the entire workflow
                                finishes.
  -o OPTION --option=OPTION     Azkaban properties. Can either be the path to
                                a properties file or a single parameter
                                formatted as `key=value`, e.g. `-o
                                user.to.proxy=foo`. For the `build` and `run`
                                commands, these will be added to the project's
                                or run's properties respectively (potentially
                                overriding existing ones). For the `info`
                                command, this will cause only jobs with these
                                exact parameters to be displayed.
  -p PROJECT --project=PROJECT  Azkaban project. Can either be a project name
                                or a path to a python module/package defining
                                an `azkaban.Project` instance. Commands which
                                are followed by an asterisk will only work in
                                the latter case. If multiple projects are
                                registered, you can disambiguate as follows:
                                `--project=module:project_name`.
  -r --replace                  Overwrite any existing file.
  -s SPAN --span=SPAN           Period to repeat the scheduled flow. Must be
                                in format `1d`, a combination of magnitude and
                                unit of repetition. If not specified, the flow
                                will be run only once.
  -t TIME --time=TIME           Time when a schedule should be run. Must be of
                                the format `hh,mm,(AM|PM),(PDT|UTC|..)`.
  -u URL --url=URL              Azkaban endpoint (with protocol, and optionally
                                a username): '[user@]protocol:endpoint'. E.g.
                                'http://azkaban.server'. The username defaults
                                to the current user, as determined by `whoami`.
                                If you often use the same url, consider using
                                the `--alias` option instead.
  -v --version                  Show version and exit.
  -x CRON --cron=CRON           Cron expression to use (e.g. `0 30 5 ? * *`).
  -z ZONE --timezone=ZONE       Timezone to use (PST|UTC|..). If unset or
                                invalid, the server default will be used. See
                                https://bit.ly/2RzHxfI for the full list.
Azkaban CLI returns with exit code 1 if an error occurred and 0 otherwise.
"""