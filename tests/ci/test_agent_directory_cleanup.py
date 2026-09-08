import gc
from pathlib import Path

from browser_use.agent.service import Agent
from browser_use.beta.service import Agent as BetaAgent
from tests.ci.conftest import create_mock_llm


def test_auto_created_agent_directory_is_removed_when_agent_is_dropped():
	agent = Agent(task='Leak nothing.', llm=create_mock_llm())
	agent_directory = agent.agent_directory
	assert agent_directory.exists()

	del agent
	gc.collect()

	assert not agent_directory.exists()


def test_user_supplied_file_system_path_survives(tmp_path):
	file_system_path = tmp_path / 'my-files'
	agent = Agent(task='Leak nothing.', llm=create_mock_llm(), file_system_path=str(file_system_path))
	assert Path(agent.file_system_path) == file_system_path

	del agent
	gc.collect()

	assert file_system_path.exists()


def test_beta_agent_auto_created_directory_is_removed_when_agent_is_dropped():
	agent = BetaAgent(task='Leak nothing.', llm=create_mock_llm())
	agent_directory = agent.agent_directory
	assert agent_directory.exists()

	del agent
	gc.collect()

	assert not agent_directory.exists()
