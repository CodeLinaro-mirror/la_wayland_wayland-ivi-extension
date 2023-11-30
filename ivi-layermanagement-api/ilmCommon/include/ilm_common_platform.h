/**************************************************************************
 *
 * Copyright (C) 2013 DENSO CORPORATION
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *        http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 ****************************************************************************/

/* Changes from Qualcomm Innovation Center are provided under the following license:

 * Copyright (c) 2023 Qualcomm Innovation Center, Inc. All rights reserved.
 * SPDX-License-Identifier: BSD-3-Clause-Clear
 */

#ifndef _ILM_COMMON_PLATFORM_H_
#define _ILM_COMMON_PLATFORM_H_

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

#include "ilm_types.h"

typedef struct _ILM_COMMON_PLATFORM_FUNC
{
    ilmErrorTypes (*init)(t_ilm_nativedisplay nativedisplay);
    t_ilm_nativedisplay (*getNativedisplay)();
    t_ilm_bool (*isInitialized)();
    ilmErrorTypes (*destroy)();
} ILM_COMMON_PLATFORM_FUNC;

extern ILM_COMMON_PLATFORM_FUNC gIlmCommonPlatformFunc;

void init_ilmCommonPlatformTable();

#ifdef __cplusplus
} /**/
#endif /* __cplusplus */

#endif /* _ILM_COMMON_PLATFORM_H_ */
