using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Gamemanager : MonoBehaviour
{
    public float totalTime;
    public Text text_Timer;
    public PlayerMove player;
    public GameObject[] stages;
    public GameObject RestartBut;
    Vector3 StartingPos;
    Quaternion StartingRotate;
    static bool isStarted = false;
    static bool isEnded=false;
    bool isPaused = false;
    public GameObject[] P_button;
    // Start is called before the first frame update

     void Awake()
     {
        Time.timeScale = 0f;

    }

    
       
        
    

    
    // Update is called once per frame
    void Update()
    {
        totalTime += Time.deltaTime;
        text_Timer.text = "시간 : " + Mathf.Round(totalTime);
    }

    void Start()
    {
        if (!isStarted)
        {
            SceneManager.LoadScene("First_s", LoadSceneMode.Single);
        }
        StartingPos = GameObject.FindGameObjectWithTag("start").transform.position;
        StartingRotate = GameObject.FindGameObjectWithTag("start").transform.rotation;
        Time.timeScale = 1f;

    }

    void OnTriggerEnter2D(Collider2D collision)
    {
    if(collision.gameObject.tag == "Player")
        {
            collision.attachedRigidbody.velocity = Vector2.zero;
            collision.transform.position = new Vector3(0, 4, -1);
        }        
    }

   public void StartGame()
    {
        
        Time.timeScale = 1f;

        GameObject standingCamera = GameObject.FindGameObjectWithTag("MainCamera");
        standingCamera.SetActive(false);

        StartingPos = new Vector3(StartingPos.x, StartingPos.y + 2f, StartingPos.z);
        Instantiate(player, StartingPos, StartingRotate);

        
    }

    public static void EndGame()
    {

        Time.timeScale = 0f;
        isEnded = true;
    }

    public static void StartMenu()
    {
        isStarted = true;
        SceneManager.LoadScene("m_Play", LoadSceneMode.Single);

    }
}
