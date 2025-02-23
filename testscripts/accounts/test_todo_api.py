import requests
import pytest
class Test_TODO_API:

    def test_todo_api(self):
        end_point_url = 'https://todo.pixegami.io'
        get_end_response = requests.get(end_point_url)
        a = get_end_response.json()
        #for x in a:
        #    print(a[x])
        assert get_end_response.status_code == 200

    def test_create_task(self):
        payload = {
            "content": "My Test Content",
            "user_id": "Rudresha C",
            "is_done": False
        }
        #Ceate Task

        end_point_url = 'https://todo.pixegami.io'

        get_create_task_response = requests.put(end_point_url + "/create-task",json=payload)

        assert get_create_task_response.status_code == 200

        get_create_data = get_create_task_response.json()

        print(get_create_data)

        task_id = get_create_data["task"]["task_id"]

        print("task_id"+ task_id)

        get_get_taskid_response = requests.get(end_point_url + f"/get-task/{task_id}")

        assert get_get_taskid_response.status_code == 200

        get_task_data = get_get_taskid_response.json()

        assert get_task_data["user_id"] == payload["user_id"]
        assert get_task_data["content"] == payload["content"]
        assert get_task_data["task_id"] == task_id

        # Update task

        payload1 = {
            "content": "My Updated Test Content",
            "user_id": payload['user_id'],
            "task_id": task_id,
            "is_done": True
        }


        get_updadate_task_response = requests.put(end_point_url + "/update-task", json=payload1)

        print(get_updadate_task_response.status_code)
        print(get_updadate_task_response.json())


        get_get_taskid_response1 = requests.get(end_point_url + f"/get-task/{task_id}")

        assert get_get_taskid_response1.status_code == 200

        print(get_get_taskid_response1.json())

        # List Tasks based on the User ID

        print("List Tasks based on user id")

        get_list_tasks_response = requests.get(end_point_url + f"/list-tasks/{payload['user_id']}")

        assert get_list_tasks_response.status_code == 200

        print(get_list_tasks_response.json())

        # delete Tasks

        print("delete task id" + task_id)

        get_delete_response = requests.delete(end_point_url + f"/delete-task/{task_id}")

        assert get_delete_response.status_code == 200

        print(get_delete_response.json())

        # List Tasks based on the User ID

        print("List Tasks based on user id after deleting the task")

        get_list_tasks_response1 = requests.get(end_point_url + f"/list-tasks/{payload['user_id']}")

        assert get_list_tasks_response1.status_code == 200

        reso = get_list_tasks_response1.json()

        if task_id in reso:
            print("task is present")
        else:
            print("task is not present")





