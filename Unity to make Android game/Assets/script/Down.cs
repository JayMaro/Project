using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Down : MonoBehaviour
{
    Animator anim;
    void Start()
    {
    anim = GameObject.Find("anim").GetComponent<Animator>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
       
    }

    void OnCollisionEnter2D(Collision2D Get)
    {
        if (Get.gameObject.layer.Equals("Platform"))
        {
            anim.SetBool("isJumping", false);
        }
    }
}
