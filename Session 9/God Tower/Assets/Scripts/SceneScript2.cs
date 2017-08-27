using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class SceneScript2 : MonoBehaviour {

	public Text levelText;
	public InputField inputField;
	public Button submitButton;
	public Text hintText;


	public string levelContent = "LEVELS";
	public string levelNumber;
	public string levelAnswer;

	string answer;

	// Use this for initialization
	void Start () {
		levelText.text = levelContent;
		StartCoroutine (ChangeLevelTextRoutine ());

	}

	public void GetInput(){
		answer = inputField.text;
		CheckAnswer (answer);
	}

	public void CheckAnswer(string answer){
		Debug.Log("Chay chua?");
		if (answer == levelAnswer) {
			hintText.text = "Yeahhhhhh!!!!!!!";
			hintText.color = Color.green;

			//TODO: Change scene
			SceneManager.LoadScene (3);

		} else {
			hintText.text = "Wronggggg!!!!!!!!";
			hintText.color = Color.red;
			inputField.text = "";
			inputField.ActivateInputField ();
		}
	}

	IEnumerator ChangeLevelTextRoutine () {
		while (true) {
			levelText.text = levelContent;
			yield return new WaitForSeconds (2f);
			levelText.text = levelNumber;
			yield return new WaitForSeconds (2f);
		}
	}

	// Update is called once per frame
	void Update () {
	}
}
